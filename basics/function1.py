# -*- coding: utf-8 -*-
# 定义求和的高阶函数
def sum(start, end, term ,next):
    if start > end:
        return 0
    else:
        return term(start) + sum(next(start), end, term, next)

# 定义对每一项的处理函数
def identity(n):
    return n

def square(n):
    return n ** 2 + 1

# 处理取下一项的函数
def next(n):
    return n + 1

# 求1 + 2 + 3 + ... + 100的和
print(sum(1, 100, identity, next))
# 求(1 x 1 + 1) +  ... + (100 x 100 + 1)的和
print(sum(1, 100, square, next))
