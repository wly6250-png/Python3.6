# -*- coding: utf-8 -*-
# 继承和多态
# Animal的subclass

'a subclass test'

__author__='Marvin Wang'

from animal import Animal

class Dog(Animal):

    def run(self): # 重写了父类的run方法
        print('Dog is running...')

class Cat(Animal):
    
    def eat(self):
        print('Eating meat...')

dog = Dog()
dog.run() # 调用子类中被重写的run方法

cat = Cat()
cat.run() # 调用父类的方法
cat.eat() # 调用子类自己的方法

# 当我们定义一个class的时候，我们实际上就定义了一种数据类型
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

# >>> from dog_cat import Dog
# Dog is running...
# Animal is running...
# Eating meat...
# >>> a = list()
# >>> a
# []
# >>> from animal import Animal
# >>> b= Animal()
# >>> b
# <animal.Animal object at 0x000000000214C710>
# >>> c = Dog()
# >>> c
# <dog_cat.Dog object at 0x000000000214C780>
# >>> isinstance(a,list)
# True
# >>> isinstance(b,Animal)
# True
# >>> isinstance(c,Dog)
# True
# >>> isinstance(c,Animal)
# True

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal()) #run_twice函数的参数是某一个类的话，参数形式:类()

run_twice(Dog())
run_twice(Cat()) # Cat并没有自己的run方法，所以调用Animal的run方法

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

# 鸭子类型test

# def一个并不继承Animal的类，但是必须要有一个run方法
class Flower(object):
    def run(self):
        print('The flower is opening...')

run_twice(Flower())
# 动态语言的鸭子类型特点决定了继承不像静态语言(java)那样是必须的
