# -*- coding: utf-8 -*-
# 类属性，对象信息操作

# 学生
class Student(object):
    # 用于记录已经注册学生数
    student_number = 0 # 类属性

    def __init__(self, name):
        self.name = name # 实例属性

# 注册一个学生:注册必填项名字，选填项利用关键字参数传递。注册完成，学生数+1
def register(name, **kw):
    a = Student(name)
    for k, v in kw.items():
        setattr(a, k, v)
    Student.student_number += 1
    return a # 返回一个追加属性k，值是v的实例对象
bob = register('Bob', score=90)
ah = register('Ah', age=8)

print(getattr(bob, 'score'))
print(getattr(ah, 'age'))
print(Student.student_number)


# >>> a = {'kkk':12,'dddd':22,'marvin':33}
# >>> a
# {'kkk': 12, 'dddd': 22, 'marvin': 33}
# >>> a.items()
# dict_items([('kkk', 12), ('dddd', 22), ('marvin', 33)])
# >>> for k, v in a.items():
# ...     print(k,v)
# ...
# kkk 12
# dddd 22
# marvin 33
