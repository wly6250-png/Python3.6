# -*- coding: utf-8 -*-

def add_end(L=None):  # 默认参数必须指向不变对象！
    if L is None:
        L=[]
    L.append('END')
    return L
