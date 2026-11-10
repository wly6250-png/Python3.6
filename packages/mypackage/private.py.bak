# -*- coding: utf-8 -*-
# 模块(Module)作用域

#正常的函数和变量名是公开的（public），可以被直接引用
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

#Python并没有一种方法可以完全限制访问private函数或变量，
#但是，从编程习惯上不应该引用private函数或变量。

'private函数和变量 test'

__author__='Marvin Wang'

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

#调用greeting()函数不用关心内部的private函数细节，
#这也是一种非常有用的代码封装和抽象的方法
#即:
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public

import sys
sys.path.append('C:\ITLMC2017\Python') # 直接修改sys.path，添加要搜索的目录
print(sys.path) # 种方法是在运行时修改，运行结束后失效

import module_test
