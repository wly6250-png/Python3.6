# -*- coding: utf-8 -*-
# Python是动态语言，
# 可以给实例动态绑定任何属性和方法，也可以给类绑定属性和方法。

class Student(object):
    pass

#给实例绑定属性
s = Student()
s.name = 'Marvin'
print(s.name)

#给实例绑定一个方法
def set_age(self,age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age,s) # 给实例绑定一个方法
s.set_age(35) # 调用实例方法,传入age参数
print(s.age) # 测试结果

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)

s2 = Student() # class的新方法，所有实例都可以继承
s2.set_score(99)
print(s2.score)

#给class绑定一个新的类属性
Student.city = 'Dalian'
print(Student.city)
setattr(s2,'city','nagoya') # 给实例s2绑定同名实力属性city
print(s2.city)
print(s.city) # 对于实例s来说，并没有自己的实例属性city，所以继承类属性city
del s2.city
print(s2.city) # 删除s2的实例属性后，也同样继承了类属性city
