# -*- coding: utf-8 -*-
# 多重继承

class Animal(object):
    pass

# 大分类
class Mammal(Animal):
    def base(self):
        print('Mannal')

class Bird(Animal):
    pass

# 各种动物
class Dog(Mammal): # 狗狗
    pass

class Bat(Mammal): # 蝙蝠
    pass

class Parrot(Bird): # 鹦鹉
    pass

class Ostrich(Bird): # 鸵鸟
    pass

# 按功能，定义Runnable和Flyable类
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying~~~')

# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog
class Dog(Mammal,Runnable):
    pass
# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat
class Bat(Mammal,Flyable):
    pass

dog = Dog()
dog.base()
dog.run()
#dog.fly()

# MixIn的概念(主线继承之外的继承，都称为MixIn)
# 在设计类的继承关系时，通常，主线都是单一继承下来的
# 如果需要“混入”额外的功能，通过多重继承就可以实现
# 让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn

class CarnivorousMixIn(object): # 肉食性
    pass
class HerbivoresMixIn(object):  # 草食性
    pass

# 改Runnable为RunnableMixIn
class RunnableMixIn(object):
    pass

class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
    pass

# MixIn的目的就是给一个类增加多个功能
# 在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，
# 而不是设计多层次的复杂的继承关系

# 只允许单一继承的语言（如Java）不能使用MixIn的设计
