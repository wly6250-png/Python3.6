# -*- coding: utf-8 -*-
# 杨辉三角
def triangles():
    L=[1] # ①
    while True:
        yield L 
        L.append(0) # 在list末尾追加一个int0，以便使list的长度+1
        L=[L[i-1]+L[i] for i in range(len(L))]
        # ②[1,0]
        # i=0,取被追加0后list的index(-1)和index(0)的数0和1相加，得到第1个元素1；
        # i=1,取被追加0后list的index(0)和index(1)的数1和0相加，得到第2个元素1；
        # ③[1,1,0]
        # i=0,index(-1)和index(0)的数0和1相加，得到第1个元素1；
        # i=1,index(0)和index(1)的数1和1相加，得到第2个元素2；
        # i=2,index(1)和index(2)的数1和0相加，得到第3个元素1；
        # ④[1,2,1,0]
        # i=0,index(-1)和index(0)的数0和1相加，得到第1个元素1；
        # i=1,index(0)和index(1)的数1和2相加，得到第2个元素3；
        # i=2,index(1)和index(2)的数2和1相加，得到第3个元素3；
        # i=3,index(1)和index(2)的数1和0相加，得到第4个元素1；

def triangles1():
    L1=[1] # ①
    while True:
        yield L1
        for i in range(1,len(L1)):
            L1[i]=pre[i]+pre[i-1]
        L1.append(1)
        pre=L1[:]
        # ②range(1,1)=[],for循环并不执行，单纯追加一个元素1,L1=[1,1]
        # ③range(1,2)=[1],i=1,L1=[1,2]⇒[1,2,1]
        # ④range(1,3)=[1,2],
        #   i=1,L1=[1,3,1]
        #   i=2,L1=[1,3,3]
        #   L1.append(1),L1=[1,3,3,1]

def triangles2():
    L=[1]
    while True:
        yield L
        L = [1] + [ L[x-1] + L[x] for x in range(1,len(L)) ] + [1]

m=int(input('请输入杨辉三角的层数:'))
n=0
for t in triangles2():
      print(t)
      n=n+1
      if n==m:
          break
      
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，
# 就是结束generator的指令，for循环随之结束
