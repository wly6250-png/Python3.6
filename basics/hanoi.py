# -*- coding: utf-8 -*-
# 汉诺塔
B=[]
def move_hanoi(n,a='A',b='B',c='C'):
    if n==1:
        print(a,'-->',c)
        B.append(a+'-->'+c)
    else:
        move_hanoi(n-1,a,c,b) #将前n-1个盘子从A移动到B上
        move_hanoi(1,a,b,c) #将最底下的最后一个盘子从A移动到C上
        move_hanoi(n-1,b,a,c) #将B上的n-1个盘子移动到C上
n=int(input('请输入汉诺塔的层数：'))
move_hanoi(n,'A','B','C')
print('总共需要操作'+str(len(B))+'次,\n'+'操作过程为:',B)

def move(n, a='A',b='B',c='C'):
    if n == 1:
        print("{0}--->{1}" .format(a,c))
    else:
        move(n-1, a,c,b)
        print("{0}--->{1}" .format(a,c))
        move(n-1, b,a,c)

# >>> a=1
# >>> b=2
# >>> c=3
# >>> print("{1}--->{0}".format(a,c))
# 3--->1
# >>> print("{0}--->{2}".format(a,c,b))
# 1--->2
# >>> print("{1}--->{2}".format(a,c,b))
# 3--->2
