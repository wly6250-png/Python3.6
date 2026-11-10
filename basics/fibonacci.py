# -*- coding: UTF-8 -*-
# ①第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))

# ②如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator

# 斐波那契数列,生成器：generator
def fib(max):
    n,a,b = 0,0,1
    while n<max:
#        print(b)
        yield b  #generator
        a,b=b,a+b # a = b,b = a+b
        n=n+1
    return 'done'

import time 
t = int(input('输入层数开始计算：'))
start =time.clock()
g=fib(t)
#i=0
K=[]
while True:
    try:
        x=next(g)
        K.append(x)
#        i=i+1
#        print('g%d:%d'%(i,x))
    # 捕获StopIteration错误
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
print(K)
end = time.clock() 
print("运算斐波拉契数列%i的时间是：%s秒" % (t , end - start))
