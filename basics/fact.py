# -*- coding: utf-8 -*-
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

#递归函数
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120

#栈溢出问题
>>> fact(1000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\ITLMC2017\Python\fact.py", line 4, in fact
    return 1
  File "C:\ITLMC2017\Python\fact.py", line 4, in fact
    return 1
  File "C:\ITLMC2017\Python\fact.py", line 4, in fact
    return 1
  [Previous line repeated 994 more times]
  File "C:\ITLMC2017\Python\fact.py", line 2, in fact
    def fact(n):
RecursionError: maximum recursion depth exceeded in comparison
