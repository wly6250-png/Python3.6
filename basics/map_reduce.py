# -*- coding: utf-8 -*-
# 为了不与Python提供的sum内置函数混淆
# 将我们自己定义的求和函数命名为Sum
from functools import reduce
def Sum(start, end, handle):
    return reduce(lambda x, y: x + y, \
                map(lambda x: handle(x), \
                    [x for x in range(start, end + 1)]))

def Product(start, end, handle):
    return reduce(lambda x, y: x * y, \
                map(lambda x: handle(x), \
                    [x for x in range(start, end + 1)]))

def accumulate(start, end, handle, combine):

    def symbol(a, b, combine):
        if '+' == combine:
            return a + b
        elif '*' == combine:
            return a * b
        else:
            pass
        
    return reduce(lambda x, y: symbol(x, y, combine), \
                map(lambda x: handle(x), \
                   [x for x in range(start, end + 1)]))

def Sum1(start, end, handle):
    return accumulate(start, end, handle, '+')

def Product1(start, end, handle):
    return accumulate(start, end, handle, '*')

# 定义handle函数
def identity(n):
    return n

print(Sum1(1,100,identity))
print(Product1(1,6,identity))
