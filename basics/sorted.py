# -*- coding: utf-8 -*-
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):    
    return t[0].lower()

L2=sorted(L,key=by_name)
print(L2)

def by_score(t):
    return t[1]

L3=sorted(L,key=by_score,reverse=True)
print(L3)

#1.sorted()函数就可以对list进行排序,作用对象是list或者iterator。
#2.key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
#3.sorted()返回的是key指定函数返回结果排序后，对应映射关系上的元序列对象list。

from operator import itemgetter
#operator模块提供的itemgetter函数用于获取对象的哪些维的数据，
#参数为一些序号（即需要获取的数据在对象中的序号）
print(sorted(L, key = itemgetter(0)))
print(sorted(L, key = itemgetter(1),reverse = True))

print(sorted(L, key = lambda x: x[0]))
print(sorted(L, key = lambda x: x[1], reverse = True))

M=[('Bob',75),('Adam',92),('bart',66),('Lisa',88),('Adam',71),('Lisa',75)]

# ①有同名的人，不同分数:('Adam',92)，('Adam',71)
# ②不同的人，有相同的分数:('Bob',75)，('Lisa',75)

# 先按名字的字母顺排序，如果有同名人的话，按分数从低到高（升顺）排序
print(sorted(M, key = itemgetter(0, 1))) #多级排序，sortkey:index(0)⇒index(1)
# 先按分数（升顺）排序，如果有相同分数的话，按名字的字母顺排序
print(sorted(M, key = itemgetter(1, 0))) #多级排序，sortkey:index(1)⇒index(0)
# 先按名字（降顺）排序，如果有同名人的话，按分数从高到低（降顺）排序
print(sorted(M, key = itemgetter(0, 1), reverse = True)) #多级排序，逆序

# 如果想要①按名字的字母顺（小写）升顺排序，②再按分数从高到低（降顺）排序
# 期待打印:
# [('Adam',92), ('Adam',71), ('bart',66), ('Bob',75), ('Lisa',88),('Lisa',75)]
def sort_2key(t):
    return(t[0].lower(),not t[1])

print(sorted(M,key=sort_2key))
