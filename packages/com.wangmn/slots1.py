# -*- coding: utf-8 -*-
# slots用于限制实例的属性和方法，不能限制类的属性和方法以及继承类实例的属性和方法

def set_city(self, city):
    self.city=city

class Student(object):
    __slots__ = ('name', 'age')
    pass

from types import MethodType
Student.set_city = MethodType(set_city, Student) # 给类绑定新的类方法
# 给类追加的方法，并不受__slots__的限制
# 通过给Student类绑定方法，实现了绑定了一个类属性，而不是实例属性

a = Student()
a.set_city('Beijing') # 调用类方法，为类属性city赋值
print(a.city)
# 所以这时，对于实例a来说，并没有实例属性city才对
del a.city # 报错！
# AttributeError: 'Student' object attribute 'city' is read-only
