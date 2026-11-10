# -*- coding: utf-8 -*-
# 访问限制，私有private，封装属性

'a class_private test'

__author__='Marvin Wang'

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' %(self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score): # 把属性封装在方法中，可以对参数做检查，避免传入无效的参数
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score') #自定义error处理
    
bart = Student('Bart Simpson',98)
#print(bart.__name)
# 实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问

#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name
print(bart._Student__name) #这样就可以直接访问__name

print(bart.get_name())
bart.set_score(100)
print(bart.get_score())

# >100，报错bad score
#bart.set_score(101) 

# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
# 是特殊变量，特殊变量是可以直接访问的，不是private变量

# 你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，
# “虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

