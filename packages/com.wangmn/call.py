# -*- coding: utf-8 -*-
# 定制类
# __call__

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

class Stu(object):

    def __init__(self,name):
        self.name = name

    def call(self): # 普通类方法
        print('My name is %s.' % self.name)

s1 = Stu('Marvin')
s1.call() # 通常我们用instance.method()来调用

class Stu1(object):

    def __init__(self):
        self.name = 'no name'

    def call(self,name):
        print('My name is %s.' % name)

s2 = Stu1()
s2.call('Bob')

class Student(object):
    
    def __init__(self,name):
        self.name = name

    def __call__(self): # 定制类方法
        print('My name is %s.' % self.name)

s3 = Student('Thomas')
s3() # 直接对实例进行调用

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
# 所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别
class Student1(object):

    def __init__(self,name):
        self.name = name

    def __call__(self,score):
        print('%s\'s score :%s' %(self.name,score))

s4 = Student1('Marry')
s4(95) # 直接对实例对象调用，并带一个参数

# 那么，怎么判断一个变量是实例对象还是函数呢？其实，更多的时候，
# 我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象

print(callable(Student1('Marry')), # 含有__call__的类实例，True
      callable(Stu1()), # 不含有__call__的类创建的对象，并不是一个可调用对象
      callable(max), # 内置函数，一定都是callable的
      callable([1,2,3]),
      callable(None),
      callable('str'))

print(callable(s4)) # Callable对象，实例对象
