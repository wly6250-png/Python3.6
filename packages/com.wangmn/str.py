# -*- coding: utf-8 -*-
# 定制类
# __str__

class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__

print(Student('Michael')) # 创建一个带参数实例对象，没有指向变量
# Student object (name:Michael)

s = Student('Thomas')
print(s)

# >>> s = Student('marivn')
# >>> s
# <str.Student object at 0x00000000029FC780>
# >>> print(s)
# Student object (name:marivn)

# 直接显示变量调用的不是__str__()，而是__repr__()，
# 两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，
# 所以，有个偷懒的写法：__repr__ = __str__

# >>> s = Student('marvin')
# >>> s
# Student object (name:marvin)
# >>> print(s)
# Student object (name:marvin)
