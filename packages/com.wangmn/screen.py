# -*- coding: utf-8 -*-
# 使用@property练习

class Screen(object):

    @property # getter方法
    def width(self):
        return self._width #函数名就是变量名，所以这里使用self._width私有变量

    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('height must be an integer')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432,'1024 * 768 = %d ?' % s.resolution
