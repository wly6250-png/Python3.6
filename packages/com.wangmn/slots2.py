# -*- coding: utf-8 -*-
# 属性分实例属性和类属性，多个实例同时更改类属性，值是最后更改的一个

def set_age(self,age):
    self.age=age

class Stu(object):
    pass

s=Stu()
a=Stu()

from types import MethodType

Stu.set_age=MethodType(set_age,Stu) # 给类绑定了方法

a.set_age(15) #调用类方法set_age，设置的类属性age的值
s.set_age(11) #也是设置类属性age的值，并把上个值覆盖掉
print(s.age,a.age) #由于a和s自身没有age属性，所以打印的是类属性age的值

a.age = 10  #给实例a添加一个属性age并赋值为10
s.age = 20  #给实例b添加一个属性age并赋值为20
#这两个分别是实例a和s自身的属性，仅仅是与类属性age同名，并没有任何关系

print(s.age,a.age)  #打印的是a和s自身的age属性值，不是类age属性值

#通过此方法在类上新增函数时，实例使用此方法实际就是引用类的方法修改类属性，
#即直接在类上新增属性

#Stu类本身并没有属性和方法，所以用这个类创建的实例也没有属性和方法。
#用MethodType将set_age方法绑定到Stu类，并不是将这个方法直接写到Stu类内部，
#而是在Stu内存中创建一个link指向外部的方法，在创建Stu实例的时候这个link也会被复制。
#所以不管创建多少实例，这些实例和Stu类都指向同一个set_age方法。
#a.set_age(15)并没有在a这个实例内部创建age属性，
#而是将age属性创建在外部set_age方法的内存区中。
#因为a和b内部link都指向外部set_age方法的内存区，
#所以不管a还是b在调用set_age方法的时候改变的是set_age方法内存区里的age属性，
#所以a改了b也就改了，如果新建一个实例c在没有调用set_age方法的前提下也会有age属性，
#因为c的link指向的set_age方法的内存区，而set_age之前被a或者b调用过了。

c = Stu()
print(c.age) # 正解！
