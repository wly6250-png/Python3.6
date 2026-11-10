# -*- coding: utf-8 -*-
# 定制类
# __getitem__

# 参考__iter__()的iter.py
# Fib实例要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

class Fib(object):
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a

f = Fib()
print(f[0],f[1],f[2],f[3],'...',f[100]) # int参数

# 但是list有个神奇的切片方法：
print(list(range(100))[5:10])

# print(f[5:10]) # 切片对象slice参数
# __getitem__()传入的参数可能是一个int，
# 也可能是一个切片对象slice，所以要做判断：

class Fib1(object):
    def __getitem__(self,n):
        if isinstance(n,int): # n是索引
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice): # n是一段切片
            start = n.start
            stop = n.stop # 这是什么表达式？
            step = n.step
            if start is None:
                start = 0
            if step is None:
                step = 1
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start and x % step == 0:
                    L.append(a)
                a,b = b,a+b
            return L

f1= Fib1()
print(f1[0],f1[1],f1[2])
print(f1[5:10],f1[:6])
print(f1[:10:2]) # 没有对step参数作处理(从索引0开始间隔2位取元素，直到小于10)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],结果来看，并没有起任何作用。
# 追加step参数处理后结果:[1, 2, 5, 13, 34]
                    
#①如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object
d={'Michael':95,'Bob':75,'Tracy':85}
print('dict is :',isinstance(d,dict))
print(d['Bob'])

class Dict(object):
    def __getitem__(self,key):
        if key == 'Michael':
            return 95
        if key == 'Bob':
            return 75
        if key == 'Tracy':
            return 85
        
d1= Dict()
print(d1['Bob'])

# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值
# 最后，还有一个__delitem__()方法，用于删除某个元素
# 我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
# 这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口

# ②__setitem__()方法实现

# ③__delitem__()方法实现
