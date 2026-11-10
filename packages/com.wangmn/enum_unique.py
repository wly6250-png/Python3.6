# -*- coding: utf-8 -*-
# 枚举类

# Python提供了Enum类,
# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
# 用Enum为枚举类型定义一个class类型,然后每个常量都是class的一个唯一实例
from enum import Enum

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun',
                      'Jul','Aug','Sep','Oct','Nov','Dec'))

# 这样我们就获得了Month类型的枚举类，
# 可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员

# 枚举支持迭代器,可以for..in遍历
for month in Month:
    print(month,',',month.name,':',month.value)

for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# value属性则是自动赋给成员的int常量，默认从1开始计数

# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12

print(Month.__members__.items())
# odict_items([('Jan', <Month.Jan: 1>), ('Feb', <Month.Feb: 2>), ('Mar', <Month.Ma
# r: 3>), ('Apr', <Month.Apr: 4>), ('May', <Month.May: 5>), ('Jun', <Month.Jun: 6>
# ), ('Jul', <Month.Jul: 7>), ('Aug', <Month.Aug: 8>), ('Sep', <Month.Sep: 9>), ('
# Oct', <Month.Oct: 10>), ('Nov', <Month.Nov: 11>), ('Dec', <Month.Dec: 12>)])

print(Month.Jan.name)
print(Month.Jan.value)
print(Month(5))
print(Month['May'])
print(Month.May)
#----------------------------------------------------------------------
# 也可以从Enum派生出自定义类:
from enum import Enum,unique

# @unique装饰器可以帮助我们检查保证没有重复value值
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0，自定义member的value值
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# 成员名Sun，Mon等等如果重复，会报TypeError: Attempted to reuse key: 'Sun'

for weekday in Weekday:
    print(weekday,',',weekday.name,':',weekday.value)

for name, member in Weekday.__members__.items():
    print(name,'=>', member)

# >>> day1 = Weekday.Mon    #Weekday.Mon是Weekday类的一个实例(成员)
# >>> day1
# <Weekday.Mon: 1>
# >>> print(day1)
# Weekday.Mon
# >>> print(day1.value)
# 1
# >>> print(Weekday.Mon.value)
# 1
# >>> print(Weekday.Mon.name) # 成员名称引用枚举常量
# Mon
# >>> print(Weekday(1))
# Weekday.Mon
# >>> print(Weekday(1).name) # 根据value的值获得枚举常量
# Mon
# >>> print(day1 == Weekday(1))
# True
# >>> Weekday(6)
# <Weekday.Sat: 6>

# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量

print(Weekday.__members__.items())
# odict_items([('Sun', <Weekday.Sun: 0>), ('Mon', <Weekday.Mon: 1>), ('Tue', <Week
# day.Tue: 2>), ('Wed', <Weekday.Wed: 3>), ('Thu', <Weekday.Thu: 4>), ('Fri', <Wee
# kday.Fri: 5>), ('Sat', <Weekday.Sat: 6>)])

# 枚举本身是class类型，父类是Enum
# 每个枚举的常量是该类型的实例，并且定义好之后不可修改

# 枚举的比较
print(Weekday.Sun is Weekday.Sun)  #同一性比较(内存地址)
print(Weekday.Sun is not Weekday.Mon)
print(Weekday.Sun == Weekday.Mon)  #值比较
print(Weekday.Sun != Weekday.Mon)
#print(Weekday.Sun < Weekday.Mon)  枚举不能比较大小
print('Weekday.Sun:',id(Weekday.Sun))
print('Weekday.Mon:',id(Weekday.Mon))
