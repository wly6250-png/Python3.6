# -*- coding: UTF-8 -*-
#偏函数(functools.partial)

#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
#返回一个新的函数，调用这个新函数会更简单。

import functools

int2 = functools.partial(int,base=2)

print(int('111000',base=2))
print(functools.partial(int,base=2)('111000'))
print(int2('111000'))

print(int2('111000',base=10))

#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
#functools.partial(func,*args,**kw)

max2 = functools.partial(max,10)
#实际上会把10作为*args的一部分自动加到左边
max2(5,6,7)
#相当于:
args = (10,5,6,7)
max(*args)

print(max2(5,6,7))
print(max(*args))
print(max2(8,9,11))

#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
#这个新函数可以固定住原函数的部分参数，从而在调用时更简单

bin2dec = functools.partial(int,base=2)
print(bin2dec('0b10001'))
print(bin2dec('10001'))

hex2dec = functools.partial(int,base=16)
print(hex2dec('0x67'))
print(hex2dec('67'))

