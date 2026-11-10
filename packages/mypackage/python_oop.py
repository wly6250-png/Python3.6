# -*- coding: utf-8 -*-
# 面向对象编程

'Object Oriented Programming'

class Student(object): #自定义的对象数据类型就是面向对象中的类（Class）

    # 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据
    def __init__(self,name,score): #__init__是Student类的构造函数，self必不可少
        # self是一个指向实例本身的引用，让实例能够访问类中的属性和方法
        self.name = name # 这样通过实例访问的变量称为“属性”,类属性
        self.score = score

    # 类的内部定义访问数据的函数，这样把“数据”给封装起来，称之为类的方法
    def print_score(self):
        print('%s:%s' %(self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson',59)
    # 调用Student类来创建一个实例对象bart，并同时为这个对象的两个属性赋值(参数)
    # 类似于java里的: Student bart = new Student('Bart Simpson',59)创建对象
lisa = Student('Lisa Simpson',87)
    # 调用class的构造方法Student()，来创建同名类的实例对象
              
bart.print_score() # 用实例化对象bart，访问类的方法print_score()
lisa.print_score() # 通过在实例上调用方法，我们就直接操作了对象内部的数据

print(bart.get_grade())

# 实例对象创建后，可以自由地给一个实例变量绑定属性
bart.age = 35 # 没有被类方法封装的属性(为实例对象追加新属性)
lisa.sex = 1  # 并不是类的属性，而是实例的属性
print(bart.age,lisa.sex)

# __init__方法是一个特殊类方法，用于创建对象的构造方法。

# 定义__init__方法，相当于为这个类设置了必须的属性
# 在创建实例的时候，把这些我们认为必须绑定的属性强制填写进去

# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，
# 必须传入与__init__方法匹配的参数，但self不需要传，
# Python解释器自己会把实例变量传进。

# __init__方法的第一个参数永远是self
# 类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
