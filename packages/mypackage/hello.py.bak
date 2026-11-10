# -*- coding: utf-8 -*-

'a test module'# 任何模块代码的第一个字符串都被视为模块的文档注释

__author__='Marvin Wang' # 使用__author__变量把作者写进去

import sys

def test():
    args = sys.argv #sys模块有一个argv变量，用list存储了命令行的所有参数。
                    #argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    print(args)     #['hello.py']
    if len(args)==1:
        print('Hello,world!')
    elif len(args)==2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

print(__name__) #当模块是直接执行的，则该变量取值为：__main__
#print(sys.path)

# C:\ITLMC2017\Python\mypackage>python hello.py
# ['hello.py']
# Hello,world!

# C:\ITLMC2017\Python\mypackage>python hello.py wangmn
# ['hello.py', 'wangmn']
# Hello,wangmn!

# C:\ITLMC2017\Python\mypackage>python hello.py wangmn wang
# ['hello.py', 'wangmn', 'wang']
# Too many arguments!

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
#而如果在其他地方导入该hello模块时，if判断将失败。

# >>> import hello
# >>> hello.test()
# ['']
# Hello,world!
# >>> hello.__name__
# 'hello'
# >>> hello.__author__
# 'Marvin Wang'
# >>> hello.__doc__
# 'a test module'

import private

print(private.__name__) # 当模块是被调用执行的，取值为模块的名字private
print(private.__author__)
print(private.__doc__)

name = ['wangmn','thomas','marvin']
print(private.greeting(name)) #public函数

print(private._private_1(name)) #private函数,私有函数同样可以被访问。


