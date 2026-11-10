# -*- coding: UTF-8 -*-
# S=π*r*r
p=3.1415926
r1=12.34
r2=9.08
r3=73.1
s1=p*r1*r1
s2=p*r2*r2
s3=p*r3*r3
print('r1:%f,面积⇒%f,\nr2:%f,面积⇒%f,\nr3:%f,面积⇒%f'%(r1,s1,r2,s2,r3,s3))

# 函数化
print('①圆面积的计算----------------------')
def area_of_circle(r):
    p=3.14
    return p*r*r

r=float(input('请输入圆半径r:'))
S=area_of_circle(r)
print('半径r:%.2f,的圆面积为:%.2f'%(r,S))

#求和1
print('②求和1+2+3+4+.....+X')
X=int(input('请输入正整数求和的最大数X:'))
def sum_of_int(X):
    sum1=0
    a1=1
    while a1<=X:
        sum1=sum1+a1
        a1=a1+1
    return sum1
print('正整数1开始到%d的连续加算结果:%d'%(X,sum_of_int(X)))

#求和2
print('③计算(1x1+1)+(2x2+1)+(3x3+1)+...+(100x100+1)')
def sum2_of_int(Y):
    sum2=0
    a2=1
    while a2<=Y:
        sum2=sum2+(a2*a2+1)
        a2=a2+1
    return sum2
SUM=sum2_of_int(100)
print('求和结果:',SUM)

#求和3
print('④计算正整数，从x到y连续加算')
def sum3_of_int(x,y):
    sum3=0
    for i in range(x,y+1):
      sum3=sum3+i
    return sum3
a=int(input('请输入正整数x:'))
b=int(input('请输入正整数y:'))
total=sum3_of_int(a,b)
print('求和正整数从x到y的结果为:',total)
