# -*- coding: utf-8 -*-
# 接受一个list并利用reduce()求积
from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
