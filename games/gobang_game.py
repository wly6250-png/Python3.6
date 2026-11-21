import pygame
import sys
from pygame.locals import *

# 初始化pygame
pygame.init()

# 中文字体候选路径（不使用 pygame.font.SysFont：它会扫描注册表，
# 注册表里有非字符串项时会抛 TypeError）
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\msyh.ttc",     # 微软雅黑
    r"C:\Windows\Fonts\simhei.ttf",   # 黑体
    r"C:\Windows\Fonts\simsun.ttc",   # 宋体
    "/System/Library/Fonts/PingFang.ttc",                      # macOS
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",          # Linux
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",  # Linux
]


def load_font(size):
    """加载支持中文的字体，找不到时退回 pygame 默认字体（中文会显示为方块）"""
    import os
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            try:
                return pygame.font.Font(path, size)
            except (OSError, pygame.error):
                continue
    return pygame.font.Font(None, size)

# 定义常量
BOARD_SIZE = 15
CELL_SIZE = 30
BOARD_WIDTH = BOARD_SIZE * CELL_SIZE
BOARD_HEIGHT = BOARD_SIZE * CELL_SIZE
MARGIN = 50
WINDOW_WIDTH = BOARD_WIDTH + 2 * MARGIN
WINDOW_HEIGHT = BOARD_HEIGHT + 2 * MARGIN
FPS = 60

# 颜色定义
BACKGROUND_COLOR = (220, 179, 92)  # 棋盘背景色
LINE_COLOR = (0, 0, 0)  # 线条颜色
BLACK = (0, 0, 0)  # 黑棋颜色
WHITE = (255, 255, 255)  # 白棋颜色
SHADOW_COLOR = (150, 150, 150)  # 棋子阴影色
HIGHLIGHT_COLOR = (255, 255, 255)  # 棋子高光色
LAST_MOVE_COLOR = (255, 0, 0)  # 最后一步标记颜色

class GobangGame:
    def __init__(self):
        self.board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = 1  # 1为黑棋，2为白棋
        self.game_over = False
        self.winner = 0
        self.last_move = None
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("五子棋游戏 - 3D效果")
        self.font = load_font(18)

    def draw_board(self):
        """绘制棋盘"""
        # 绘制棋盘背景
        self.screen.fill(BACKGROUND_COLOR)
        
        # 绘制网格线
        for i in range(BOARD_SIZE):
            # 水平线
            pygame.draw.line(
                self.screen, 
                LINE_COLOR, 
                (MARGIN, MARGIN + i * CELL_SIZE), 
                (WINDOW_WIDTH - MARGIN, MARGIN + i * CELL_SIZE), 
                1
            )
            # 垂直线
            pygame.draw.line(
                self.screen, 
                LINE_COLOR, 
                (MARGIN + i * CELL_SIZE, MARGIN), 
                (MARGIN + i * CELL_SIZE, WINDOW_HEIGHT - MARGIN), 
                1
            )
            
        # 绘制天元和星位
        star_points = [3, 7, 11]
        for i in star_points:
            for j in star_points:
                pygame.draw.circle(
                    self.screen, 
                    LINE_COLOR, 
                    (MARGIN + i * CELL_SIZE, MARGIN + j * CELL_SIZE), 
                    4
                )
    
    def draw_stone_3d(self, x, y, color):
        """绘制3D效果的棋子"""
        # 计算棋子位置
        pos_x = MARGIN + x * CELL_SIZE
        pos_y = MARGIN + y * CELL_SIZE
        
        radius = CELL_SIZE // 2 - 2

        # 先绘制半透明阴影（pygame.draw 直接画到屏幕会忽略 alpha，
        # 所以画在带 SRCALPHA 的临时 Surface 上），再画棋子，避免阴影盖住棋子
        shadow_offset = 3
        size = (radius + 2) * 2
        shadow = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(shadow, (0, 0, 0, 90), (size // 2, size // 2), radius)
        self.screen.blit(shadow, (pos_x - size // 2 + shadow_offset, pos_y - size // 2 + shadow_offset))

        # 绘制棋子主体
        pygame.draw.circle(self.screen, color, (pos_x, pos_y), radius)
        if color == WHITE:
            pygame.draw.circle(self.screen, (170, 170, 170), (pos_x, pos_y), radius, 1)

        # 绘制高光（制造3D效果）
        highlight_pos = (pos_x - 4, pos_y - 4)
        highlight_color = (110, 110, 110) if color == BLACK else (235, 235, 235)
        pygame.draw.circle(self.screen, highlight_color, highlight_pos, CELL_SIZE // 6)
    
    def draw_pieces(self):
        """绘制棋子"""
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] != 0:
                    if self.board[row][col] == 1:
                        color = BLACK
                    else:
                        color = WHITE
                    
                    self.draw_stone_3d(col, row, color)
        
        # 标记最后一步
        if self.last_move:
            x, y = self.last_move
            pos_x = MARGIN + x * CELL_SIZE
            pos_y = MARGIN + y * CELL_SIZE
            pygame.draw.circle(
                self.screen, 
                LAST_MOVE_COLOR, 
                (pos_x, pos_y), 
                CELL_SIZE // 4, 
                2
            )
    
    def check_win(self, x, y):
        """检查是否获胜"""
        player = self.board[y][x]
        
        # 检查四个方向：水平、垂直、两个对角线
        directions = [
            [(1, 0), (-1, 0)],   # 水平
            [(0, 1), (0, -1)],   # 垂直
            [(1, 1), (-1, -1)],  # 主对角线
            [(1, -1), (-1, 1)]   # 反对角线
        ]
        
        for direction in directions:
            count = 1  # 当前位置的棋子
            
            for dx, dy in direction:
                tx, ty = x, y
                while True:
                    tx += dx
                    ty += dy
                    if (
                        tx < 0 or tx >= BOARD_SIZE or 
                        ty < 0 or ty >= BOARD_SIZE or 
                        self.board[ty][tx] != player
                    ):
                        break
                    count += 1
                
            if count >= 5:
                return True
        
        return False
    
    def make_move(self, x, y):
        """下棋"""
        if self.game_over or self.board[y][x] != 0:
            return False
            
        self.board[y][x] = self.current_player
        self.last_move = (x, y)
        
        if self.check_win(x, y):
            self.game_over = True
            self.winner = self.current_player
            return True

        # 棋盘下满且无人获胜：平局
        if all(cell != 0 for row in self.board for cell in row):
            self.game_over = True
            self.winner = 0
            return True

        self.current_player = 3 - self.current_player  # 切换玩家 (1->2, 2->1)
        return True
    
    def get_board_pos(self, mouse_x, mouse_y):
        """根据鼠标位置获取棋盘坐标"""
        # 检查是否在棋盘范围内
        if (mouse_x < MARGIN - CELL_SIZE // 2 or 
            mouse_x > WINDOW_WIDTH - MARGIN + CELL_SIZE // 2 or
            mouse_y < MARGIN - CELL_SIZE // 2 or 
            mouse_y > WINDOW_HEIGHT - MARGIN + CELL_SIZE // 2):
            return None, None
        
        # 找到最近的交叉点
        col = round((mouse_x - MARGIN) / CELL_SIZE)
        row = round((mouse_y - MARGIN) / CELL_SIZE)
        
        # 检查是否在棋盘内
        if 0 <= col < BOARD_SIZE and 0 <= row < BOARD_SIZE:
            return int(col), int(row)
        else:
            return None, None
    
    def draw_status(self):
        """绘制游戏状态"""
        font = self.font

        if self.game_over:
            if self.winner == 0:
                winner_text = "平局!"
            else:
                winner_text = "黑棋获胜!" if self.winner == 1 else "白棋获胜!"
            text = font.render(winner_text, True, (255, 0, 0))
        else:
            player_text = "黑棋回合" if self.current_player == 1 else "白棋回合"
            text = font.render(player_text, True, (0, 0, 0))
        
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_WIDTH // 2, 20)
        self.screen.blit(text, text_rect)
        
        # 绘制重新开始提示
        restart_text = font.render("按 R 键重新开始", True, (0, 0, 0))
        restart_rect = restart_text.get_rect()
        restart_rect.center = (WINDOW_WIDTH // 2, 40)
        self.screen.blit(restart_text, restart_rect)
    
    def reset_game(self):
        """重置游戏"""
        self.board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = 1
        self.game_over = False
        self.winner = 0
        self.last_move = None
    
    def run(self):
        """运行游戏"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    # 鼠标左键点击
                    x, y = self.get_board_pos(event.pos[0], event.pos[1])
                    if x is not None and y is not None:
                        self.make_move(x, y)
                elif event.type == KEYDOWN:
                    if event.key == K_r:
                        # 按R键重新开始
                        self.reset_game()
            
            # 绘制游戏界面
            self.draw_board()
            self.draw_pieces()
            self.draw_status()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = GobangGame()
    game.run()