# -*- coding: UTF-8 -*-
# 使用@property

class Student(object):

    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0～100')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())

# Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student1(object):

    @property   # 把一个getter方法变成属性
    def score(self):
        return self._score

    @score.setter  # 把一个setter方法变成属性赋值
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0～100')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property  # 只定义getter方法，不定义setter方法就是一个只读属性
    def age(self):
        return 2017 - self._birth

d = Student1()
d.score = 60 # OK，实际转化为d.set_score(60)
print(d.score) # OK，实际转化为d.get_score()

#d.score = 999 # ValueError

d.birth = 1982
print(d.birth)
print(d.age)
#d.age = 30 # AttributeError: can't set attribute

