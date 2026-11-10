# -*- coding: utf-8 -*-
# 多重继承，同名方法的优先顺问题(MRO的C3算法)

#生父
class Father():

    def func(self):
        print('生父打儿子')

#隔壁老王
class LaoWang():

    def func(self):
        print('老王打儿子')
    def func1(self):
        print('跟你妈说明天下午我会来')
#继父
class StepFather():

    def func(self):
        print('继父打儿子')
    def func1(self):
        print('我还会打你妈')

#神秘人
class Mysterious(Father,LaoWang,StepFather):
    pass

#让我们看看到底谁打了儿子
s=Mysterious()
s.func()
s.func1()

#结论:
#多重继承中如果有同名的方法，顺位靠前(最左边)的父类中的该当方法有效。
#多重继承的格式，MRO机制: http://python.jobbole.com/85685/
# 子类(生父，继父1，继父2，...)

class D(object):
    pass
 
class E(object):
    pass
 
class F(object):
    pass
 
class C(D, F):
    pass
 
class B(E, D):
    pass
 
class A(B, C):
    pass
 
if __name__ == '__main__':
    print(A.__mro__)
    # A⇒B⇒E，⇒C⇒D⇒F，⇒object (拓扑排序算法)
