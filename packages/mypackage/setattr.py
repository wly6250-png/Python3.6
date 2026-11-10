# -*- coding: utf-8 -*-
# 使用setattr()来操作一个对象或类的状态

'a setattr test'

__author__='Marvin Wang'

class c():
    pass

setattr(c,'test',lambda self,x : x*x) # 为类c增加新的类方法'test'
d = c() # 创建类c的实例对象d

print(d.test(2)) # 实例d调用追加的方法test()
print(c().test(2)) # 未指向任何实例变量的对象，调用方法test()
# c.test(2) ⇒ 报错！lambda定义了self参数，类名调用时需要指定self参数
print(c.test(None,2)) # 类名直接调用类方法test()，为self设置参数None
# d.test(None,2) ⇒ 报错！实例对象的方法调用，并不需要self

setattr(d,'new',lambda y : y*10) # 为实例对象d增加新的方法'new'
print(d.new(2))
# print(c.new(2)) ⇒ 报错！type object 'c' has no attribute 'new'

setattr(c,'fn',lambda z : z+1) # 这样，相当于为类c追加了一个指向函数的类属性fn
print(c.fn(2)) # 相当于定义了一个类属性 fn = lambda z : z+1
print(hasattr(d,'fn')) # True，属性fn存在
# print(d.fn(2)) ⇒ 报错！<lambda>() takes 1 positional argument but 2 were given
# print(d.fn(None,2)) ⇒ 同样报错！

setattr(c,'sq',abs) # 追加了一个类属性sq = abs
print(c.sq(-2)) # 2
print(d.sq(-2)) # 2 实例d继承了类属性sq，并同样指向函数abs
print(dir(d))
print(dir(c)) # 相对于实例对象d，少了上面的方法'new'

#结论:如果以lambda方式为class追加一个函数的属性，如果不指定self参数，
#将被视为给该类追加了一个指向该函数的属性，而不是一个类方法。

print(type(d)) #实例对象<class '__main__.c'>
print(type(c)) #类<class 'type'>

print(hasattr(d,'test')) # True
print(hasattr(d,'new')) # True
print(getattr(c(),'new',404)) # 404
print(hasattr(c,'test')) # True
print(hasattr(c,'new')) # False
print(hasattr(c,'fn')) # True

#结论就是在class中def method和setattr添加的自定义函数均会被认为是bound method

#class属性指向函数的例子:
#その①
class My():
    def __init__(self):
        self.a = abs

my = My()
print(my.a)
print(my.a(-1))
#その②
class Lam():
    def __init__(self):
        self.a = lambda x : x*x

lam = Lam()
print(lam.a)
print(lam.a(5))

setattr(Lam,'sq',abs) # 类属性，相当于sq = abs
print(lam.sq)
print(lam.sq(-2)) #实例lam继承了类属性sq
print(Lam.sq(-2)) #类名调用类方法sq
