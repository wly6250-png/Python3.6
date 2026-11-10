# -*- coding: utf-8 -*-
# 过滤器
# filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

def is_odd(n):
    return n%2==1

print(list(filter(is_odd,[1,2,4,5,6,9,15])))

# strip() 方法用于移除字符串头尾指定的字符（默认为空格）
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A','','B',None,'C','  '])))

# 素数(2以外的素数一定是奇数，奇数不一定是素数)
L=list(range(2,101))

def _n1_odd(s):
    return s%2!=0

L1=list(filter(_n1_odd,L))
print(L1)

def _n2_odd(s):
    return s%3!=0

L2=list(filter(_n2_odd,L1))
print(L2)
#-------------------------------------------
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n),it) # 构造新序列

# 第一次:
# n=2,返回2
# 第二次:
# it[3,5,7,9,11,13,15,17......]
# next(it),n=3,返回3
# 第三次:
# n=3,过滤序列it[5,7,9,11....]⇒[5,7,11,....]
# next(it),n=5,返回5
# 第四次:
# n=5,过滤序列it[7,11,13,17,19,21,23,25,27....]⇒[7,11,13,17,19,21,23,27....]
# next(it),n=7,返回7

# it=[3,5,7,9,....]
#  n是每次next从it序列里取出的第一个数

# 打印1000以内的素数
L=[]
for n in primes():
    if n < 1000:
        L.append(n)
    else:
        break
print(L)
#----------------------------------
from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return n

P=[]      
for n in range(1,1000):
    if is_prime(n) != False:
        P.append(n)
print(P)
