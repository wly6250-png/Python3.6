# -*- coding: utf-8 -*-
# 函数式编程Functional Programming
# ①求和
def sum(start,end,handle):
    total = 0
    for x in range(start,end+1):
        total += handle(x)
    return total

# 定义处理的handle函数
# 求1到100的和
def ident(n):
    return n

print(sum(1,100,ident))

# 求1到100每项平方加1的和
def square_plus_one(n):
    return n**2+1

print(sum(1,100,square_plus_one))

# 求1到100的立方和
def cube(n):
    return n**3

print(sum(1,100,cube))

# 求1到100所有素数的和
# 质数又称素数。一个大于1的自然数，除了1和它自身外，
# 不能被其他自然数整除的数叫做质数；否则称为合数.

# 对正整数n，如果用2到sqrt(n)之间的所有整数去除，均无法整除，则n为质数。
# 处理函数is_prime用于判断一个正整数是否为素数
# 如果是素数的话，则返回这个素数n
# 否则则返回False
from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return n

print(sum(1, 100, is_prime))

# ②求积
#1到n的阶乘函数式
def product(start,end,handle):
    total=1
    for x in range(start,end+1):
        total *= handle(x)
    return total

def factroial(n):
    return product(1,n,ident)

print(product(1,10,ident))
print(factroial(10))

def n_plus_n(n):
    return n+n

print(product(1,10,n_plus_n)) #(1+1)*(2+2)*....*(10+10)
print(product(1,10,square_plus_one))

def factroial_n1(n):
    return product(1,n,n_plus_n) # (1+1)*(2+2)*(3+3)....*(n+n)

print(factroial_n1(3))

# ③累积
def accmuluate(start,end,handle,init_value,combine):

    def symbol(a,b,combine):
        if combine == '+':
            return a+b
        elif combine == '*':
            return a*b
        else:
            pass #错误处理

    total=init_value
    for x in range(start,end+1):
        total=symbol(total,handle(x),combine)
    return total

def sum1(start,end,handle):
    return accmuluate(start,end,handle,0,'+')

def product1(start,end,handle):
    return accmuluate(start,end,handle,1,'*')

# 0+1+2+3+....+100
print(sum1(1,100,ident))
# 1*(1+1)*(2+2)*....*(10+10)
print(product1(1,10,n_plus_n))
# 0+(1*1+1)+(2*2+1)+....+(n**2+1)
print(sum1(1,10,square_plus_one))
