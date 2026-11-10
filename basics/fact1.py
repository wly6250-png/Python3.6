# -*- coding: utf-8 -*-
# 递归函数的尾递归写法

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)

>>> fact(5)
120
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120

#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题
>>> fact(1000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\ITLMC2017\Python\fact1.py", line 5, in fact
    return fact_iter(n,1)
  File "C:\ITLMC2017\Python\fact1.py", line 10, in fact_iter
    return fact_iter(num-1,num*product)
  File "C:\ITLMC2017\Python\fact1.py", line 10, in fact_iter
    return fact_iter(num-1,num*product)
  File "C:\ITLMC2017\Python\fact1.py", line 10, in fact_iter
    return fact_iter(num-1,num*product)
  [Previous line repeated 993 more times]
  File "C:\ITLMC2017\Python\fact1.py", line 8, in fact_iter
    if num==1:
RecursionError: maximum recursion depth exceeded in comparison
