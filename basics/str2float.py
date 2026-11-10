# -*- coding: utf-8 -*-
# str转换为float
from functools import reduce

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, \
            '7': 7, '8': 8, '9': 9}[s]

def str2float(s):
    d=s
    if s.find('-')==0:
        s=s.strip('-')
    p=s.find('.')
    end=len(s)-1
    if p==-1:
        a = reduce(lambda x,y:x*10+y,map(char2num,s))*1.0
    elif p==0:
        a = reduce(lambda x,y:x*10+y,map(char2num,s[p+1:]))/10**(end-p)
    else:
        a = reduce(lambda x,y:x*10+y,map(char2num,s[:p])) \
            + reduce(lambda x,y:x*10+y,map(char2num,s[p+1:]))/10**(end-p)
    if d.find('-')==0:
        a = a*-1
    return a

print(float('123.456'))
print(float('01203.40560'))
print(float('12345'))
print(float('.12345'))
print(float('-123.45'))             
print('str2float(\'123.456\') =',str2float('123.456'))
print('str2float(\'01203.40560\') =',str2float('01203.40560'))
print('str2float(\'12345\') =',str2float('12345'))
print('str2float(\'.12345\') =',str2float('.12345'))
print('str2float(\'-123.45\') =',str2float('-123.45'))

print('方法2--------------------------')
import math
def str2float1(s):
    if s.find('.')==-1:
        return reduce(lambda x,y:x*10+y,map(char2num,s))*1.0
    elif s.find('.')==0:
        s1, s2 = s.split('.', 1)
        return reduce(lambda x,y:x*10+y, map(char2num,s2))/pow(10,len(s2))
    else:
        s1, s2 = s.split('.', 1)
    return reduce(lambda x,y:x*10+y, map(char2num, s1+s2))/pow(10,len(s2))

print('str2float(\'123.456\') =',str2float1('123.456'))
print('str2float(\'01203.40560\') =',str2float1('01203.40560'))
print('str2float(\'12345\') =',str2float1('12345'))
print('str2float(\'.12345\') =',str2float1('.12345'))
#print('str2float(\'-123.45\') =',str2float1('-123.45'))
