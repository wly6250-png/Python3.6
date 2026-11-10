# -*- coding: utf-8 -*-
# 继承和多态

'a class-subclass test'

__author__='Marvin Wang'

class Animal(object):

    def run(self):
        print('Animal is running...')

# subclass: 参照py文件dog_cat.py

# 静态语言 vs 动态语言

#对于静态语言（例如Java）来说，
#如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，
#否则，将无法调用run()方法。

#对于Python这样的动态语言来说，
#则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了。

#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系

#Python的“file-like object“就是一种鸭子类型
