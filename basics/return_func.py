# -*- coding: utf-8 -*-
#函数作为返回值

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
print(f)
#调用函数f()时，才真正计算求和的结果
print(f())

#我们在函数lazy_sum中又定义了函数sum，并且内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
#这种称为“闭包（Closure）”的程序结构拥有极大的威力

#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
#>>> f1= lazy_sum(1,3,5,7,9)
#>>> f1
#<function lazy_sum.<locals>.sum at 0x0000000000653E18>
#>>> f2= lazy_sum(1,3,5,7,9)
#>>> f2
#<function lazy_sum.<locals>.sum at 0x0000000001FEC268>
#>>> f1==f2
#False

#------------闭包（Closure）-----------------------
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()

#当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
#i=1,fs=[f(1*1)]
#i=2,fs=[f(2*2),f(2*2)]
#i=3,fs=[f(3*3),f(3*3),f(3*3)]

print(f1())
print(f2())
print(f3())

#返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
#它们所引用的变量i已经变成了3，因此最终结果都为9

#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量

#解决办法:再创建一个函数，用该函数的参数绑定循环变量当前的值，
#         无论该循环变量后续如何更改，已绑定到函数参数的值不变

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
    return fs

fa,fb,fc = count1()
# fs=[i=1的闭包函数f(1)，i=2的闭包函数f(2)，i=3的闭包函数f(3)]
# fa = i=1的闭包函数f(1)
# fb = i=2的闭包函数f(2)
# fc = i=3的闭包函数f(3)
# 需要注意:此时还是以闭包保存了参数和变量，没有被实行。
# 下面调用fa()的时候才实行这个闭包。
print(fa())
print(fb())
print(fc())

# 所以呢，如果按下面这个来赋值给fk的话，相当于fk是一个保存多个函数的list
fk = count1()

print(fk[0](),fk[1](),fk[2]())

#-------------非闭包list，而是一个执行后结果的list------------
def count2():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f())
    return fs

f4,f5,f6 = count2()
fx=count2()
fy=count2()
fz=count2()

print(f4)
print(f5)
print(f6)

print(fx,fy,fz)
#----------------利用lambda函数缩短代码------------------

count3 = lambda: [(lambda j: lambda: j * j)(i) for i in range(1, 4)]

Fa,Fb,Fc = count3()

print(Fa(),Fb(),Fc())
