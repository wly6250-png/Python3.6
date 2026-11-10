# -*- coding: UTF-8 -*-
#匿名函数

a = list(map(lambda x: x*x,[1,2,3,4,5,6,7,8,9]))
print(a)

f = lambda x: x*x
print(f)
print(f(5))

def build(x,y):
    return lambda: x*x+y*y

print(build(1,2))

b = build(1,2)
print(b())

#关键字lambda表示匿名函数，冒号前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

def make(n):
    return lambda x: x+n

f1=make(42) #参数n=42,返回一个函数，没有被实行的闭包

print(f1(0)) #f1的参数是x=0,实行这个闭包，打印结果
print(f1(1))

def func1():
    x,y=1,2
    return lambda m=x,n=y:m+n
print(func1()()) #输出3

def func2():
    x,y=1,2
    return lambda m=x,n=y:m+n
print(func2()(3,7)) #输出10

#这里x从0迭代到4的时候每次都会先赋值给n,
#所以返回的"闭包"中参数n是绑定的，不会因为x的变化而变化
def func3():
    squares = []
    for x in range(5):
        squares.append(lambda n=x: n**2)
    return squares

a,b,c,d,e = func3()

print(a(),b(),c(),d(),e())
