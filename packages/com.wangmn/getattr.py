# -*- coding: utf-8 -*-
# 定制类
# __getattr__

class Student(object):

    def __init__(self):
        self.name = 'Marvin'

# Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
    def __getattr__(self,attr):
        if attr == 'score':
            return 99       #返回一个属性

        if attr == 'age':
            return lambda: 25 #返回一个函数

        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
        
# 当调用不存在的属性时，比如score，Python解释器会试图调用
# __getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值

s = Student()
print(s.name)  # 调用存在的属性
print(s.score) # 调用不存在的属性
print(s.age()) # 调用不存在的函数

# 注意，只有在没有找到属性的情况下，才调用__getattr__，
# 已有的属性，比如name，不会在__getattr__中查找

# python定义的__getattr__默认返回就是None，如果是没有在__getattr__里定义的
# 属性就都会返回None。
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：

# print(s.abc) # 如果没raise处理，就返回None
# 如果有AttributeError的错误处理，就不再返回None，而是返回定义的内容

# 利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):

    def __init__(self,path=''):
        self._path = path

    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)
# /status/user/timeline/list

# 还有些REST API会把参数放到URL中,
# 调用时，需要把:user替换为实际用户名
class Chain1(object):

    def __init__(self,path=''):
        self._path = path

    def __getattr__(self,path):
        return Chain1('%s/%s' % (self._path,path))

    def __str__(self):
        return self._path

    __repr__ = __str__
    
    #只需添加如下的 __call__() 函数即可
    def __call__(self,path):
        return Chain1('%s/%s' % (self._path,path))
    
print(Chain1().users('michael').repos)
# /users/michael/repos
print(Chain1().status.user.timeline.list)
