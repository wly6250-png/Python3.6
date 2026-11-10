# -*- coding: utf-8 -*-
#装饰器(decorator),在代码运行期间动态增加功能的方式，称之为“装饰器”

def log(func): #函数func作为参数
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__) #装饰器的主体，被增加的功能
        return func(*args,**kw)
    return wrapper  #返回一个函数

#借助Python的@语法，把decorator置于函数的定义处
@log  # 相当于执行了语句: now = log(now)
def now():
    print('2017-7-10')

now()
print('now.__name__:',now.__name__)

#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
#只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，
#即在log()函数中返回的wrapper()函数。

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log1(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log1('execute') # 相当于:now1 = log1('execute')(nwo1)
def now1():
    print('2017-8-31')

now1()

#首先执行log1('execute')，返回的是decorator函数，
#再调用返回的函数，参数是now1函数，返回值最终是wrapper函数

print('now1.__name__:',now1.__name__)
#经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
#需要把原始函数的__name__等属性复制到wrapper()函数中，
#否则，有些依赖函数签名的代码执行就会出错.

# 一个完整的decorator的写法:
import functools

def log2(func):
    @functools.wraps(func) # Python内置的functools.wraps函数
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log2
def now2():
    print('2018-1-1')
    
now2()
print('now2.__name__:',now2.__name__)

#带参数decorator
import functools

def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log3('execute') # 相当于:now3 = log3('execute')(nwo3)
def now3():
    print('2017-9-29')

now3()
print('now3.__name__:',now3.__name__)
