# -*- coding: utf-8 -*-
# 使用__slots__
# Python允许在定义class的时候，定义一个特殊的__slots__变量，
# 来限制该class实例能添加的属性。

'a slots test'

__author__='Marvin Wang'

class Student(object):
    __slots__ = ('name','age') # 用tuple定义允许绑定的实例属性名称

s = Student()
s.name = 'thomas'
s.age = 35
print(s.name)
print(s.age)

# s.score = 99
# AttributeError: 'Student' object has no attribute 'score'

Student.score = 99
print(Student.score) # slots并不能限制类属性的绑定

#注意:__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class SubStudent(Student): # 创建一个Student的子类
    pass

g = SubStudent()  # 创建子类的实例对象
g.score = 999 # 绑定一个实例属性score
print(g.score) # 测试

# 如果在子类中也定义__slots__，那这个子类实例允许定义的属性是？
class Student1(Student):
    __slots__ = ('score','sex')

d = Student1()

d.sex = 'man'
print(d.sex)

d.name = 'marvin'
print(d.name)

# d.city = 'dalian'
# AttributeError: 'Student1' object has no attribute 'city'

#结论:
#在子类中也定义__slots__，
#子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

#注意:如果父类中没有__solts__，子类的__solts__将不起任何作用，
#     因为子类于父类的__solts__是并集的关系。

#① 父：__slots__=() and 子:__solts__=('score','sex')
# 对于父类来说，实例将不能动态绑定任何实例属性
# 对于子类来说，实例只能绑定实例属性'score','sex'

#② 父: __slots__没有定义(无限制) and 子:__solts__=('score','sex')
# 父类来说，实例属性的绑定没有任何限制
# 子类来说，因为父类是无限制，所以子类的__solts__不起任何限制作用

#疑问:是否可以为类动态绑定 __slots__特殊变量(子类SubStudent为例)

# setattr(SubStudent,'__slots__',('score','sex'))
# print(getattr(SubStudent,'__slots__',404))

SubStudent.__slots__=('score','sex')
print(hasattr(SubStudent,'__slots__'))
print(dir(g))

g.sex = 'man'
print(g.sex)

g.city = 'dalian' # 结论是，特殊变量__slots__不能动态绑定
print(g.city)

