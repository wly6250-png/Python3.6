# -*- coding: UTF-8 -*-
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def person(name,age,**kw):  # 关键字参数
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:',name,'age:',age,'other:',kw)

def person1(name,age,*,city,job): # 命名关键字参数,只接收city和job作为关键字参数
    print(name,age,city,job)

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person2(name,age,*args,city='Dalian',job): # 'Dalian'为命名关键字参数的缺省值，而非默认参数
    print(name,age,args,city,job)

def f1(a, b, c=0, *args, **kw): # 可变参数，关键字参数
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw): # 命名关键字，关键字
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它
def func(*args,**kw):
    print('args:',args)
    print('kw:',kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}

f1(args,kw)
f1(*args,kw)
f1(*args,*kw)
f1(*args,**kw)


#>>> args = (1, 2, 3, 4)
#>>> kw = {'d': 99, 'x': '#'}
#>>> f1(args,kw)
#a = (1, 2, 3, 4) b = {'d': 99, 'x': '#'} c = 0 args = () kw = {}
#>>> f1(*args,kw)
#a = 1 b = 2 c = 3 args = (4, {'d': 99, 'x': '#'}) kw = {}
#>>> f1(*args,*kw)
#a = 1 b = 2 c = 3 args = (4, 'd', 'x') kw = {}
#>>> f1(*args,**kw)
#a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
