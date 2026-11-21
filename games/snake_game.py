import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 设置游戏窗口
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20
GAME_SPEED = 15

# 定义方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 创建游戏窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('贪吃蛇')
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = self.direction
        self.color = GREEN
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, new_direction):
        """请求转向。与“当前实际前进方向”比较，禁止原地掉头；
        同一帧内多次按键只有合法的最后一次生效，且不会出现先转再反向的情况。"""
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.next_direction = new_direction

    def update(self):
        self.direction = self.next_direction
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x*BLOCK_SIZE)) % WINDOW_WIDTH, (cur[1] + (y*BLOCK_SIZE)) % WINDOW_HEIGHT)
        if new in self.positions[3:]:
            return False
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def reset(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = self.direction
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], BLOCK_SIZE, BLOCK_SIZE))

class Food:
    def __init__(self, occupied=()):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position(occupied)

    def randomize_position(self, occupied=()):
        """随机生成食物位置，避开 occupied（通常是蛇身所在格子）"""
        occupied = set(occupied)
        free = [(x, y)
                for x in range(0, WINDOW_WIDTH, BLOCK_SIZE)
                for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE)
                if (x, y) not in occupied]
        if free:
            self.position = random.choice(free)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

def main():
    snake = Snake()
    food = Food(snake.positions)
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)

        # 更新蛇的位置
        if not snake.update():
            snake.reset()
            food.randomize_position(snake.positions)

        # 检查是否吃到食物
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position(snake.positions)

        # 绘制游戏界面
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        
        # 显示分数
        score_text = font.render(f'Score: {snake.score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.update()
        clock.tick(GAME_SPEED)

if __name__ == '__main__':
    main()
