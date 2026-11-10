# -*- coding: utf-8 -*-
#装饰器decorator test1
#函数调用的前后打印出'begin call'和'end call'的日志

import functools
import time

#无参数
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('begin call %s():' % func.__name__)
        fun = func(*args,**kw)
        print('end call %s():' % func.__name__)
        return fun
    return wrapper

@log  # now = log(now),用元函数now做参数调用log函数，把返回的函数赋给变量now
def now():
    print('now is:'+time.asctime()) #当前的日时信息

now()

#带参数
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s begin call %s():' %(text,func.__name__))
            func(*args,**kw)
            print('%s end call %s():' %(text,func.__name__))
            return
        return wrapper
    return decorator

@log1('time show') # now1 = log1('time show')(now)
                   # log1('time show') ⇒ 返回函数 decorator
                   # 然后再把函数now作业参数调用decorator(now)
def now1():
    print('now is:'+time.asctime())

now1()
        
#装饰器通用参数格式
def log2(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            if isinstance(text,(int,str)):
                print('%s begin call %s():' %(text,func.__name__))
                func(*args,**kw)
                print('%s end call %s():' %(text,func.__name__))
            else:
                print('begin call %s():' % func.__name__)
                func(*args,**kw)
                print('end call %s():' % func.__name__)
            return
        return wrapper
    return decorator if isinstance(text,(int,str)) else decorator(text) 

@log2 # now2 = log2(now2),相当于decorator(nows2)
def now2():
    print('now is:'+time.asctime())

now2()

@log2('timeshow') # now3 = log2('timeshow')(now3)
def now3():
    print('now is:'+'2017-07-10')

now3()


