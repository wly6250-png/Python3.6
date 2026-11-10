# -*- coding: utf-8 -*-
# 类和实例

class People: #Python3开始可以省略继承的类(object)

    def __init__(self,name,height,age,sex=0): #类属性定义，初期化函数，构造方法
        self.name = name
        self.height = height
        self.age = age
        self.sex = sex

    def get_height(self):
        return self.height

    def set_height(self,height):
        self.height = height

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age

    def get_sex(self): # 理论上性别不能被修改，所以没有设置set方法
        return self.sex

    def get_name(self):
        return self.name

    def set_name(self,name): 
        self.name = name

    def cry(self):
        print('我在哭')

    def laugh(self):
        print(self.name+'在笑')

    def printBaseMes(self):
        print(self.name+'的身高是:'+self.height+'cm')
        print(self.name+'的年龄是:',self.age,'才')
        if self.sex == 0:
            print('TA是个爷们')
        else:
            print('TA是个姑娘')

if __name__=='__main__':
    me = People('marvin','178',35) #sex是默认属性，有初期值
    other = People('thomas','165',29,1)

    me.job = 'IT' # 追加实例属性
    print(me.get_name()+'的工作是:'+me.job)

    me.laugh()
    other.cry()
    me.printBaseMes()
    other.printBaseMes()

    name = input(me.get_name()+' change name to:')
    me.set_name(name)
    me.laugh()
    me.printBaseMes()

    print(other.get_name()+'去年的身高:'+other.get_height()+'cm')
    other.set_height('180')
    other.printBaseMes()
