# -*- coding: utf-8 -*-
# 类的继承和多态
# 父类:class_object.py 的 People类

'a __init__() of subclass test'

__author__='Marvin Wang'

from class_object import People

class Ibmer(People):

    def __init__(self,name,height,age,sex,sn):
        # 调用父类的init构造方法，实现在子类中再定义父类中已有的属性
        super(Ibmer,self).__init__(name,height,age,sex)
        #或者:s.__init__(self,name,height,age,sex)
        self.__sn = sn # 子类中新的属性,私有属性private

    # 添加一个子类的新方法
    def sn_number(self):
        print(self.name+'的员工号:'+self.__sn)

    def get_sn(self):
        return self.__sn

    def set_sn(self,sn):
        self.__sn = sn

if __name__=='__main__':
    marvin = Ibmer('marvin','178',35,1,'BI943949')
    marvin.sn_number()

    print(marvin.get_name()+'的员工号:'+marvin.get_sn())
    sn = input('新员工号变更为:')
    marvin.set_sn(sn)
    print(marvin.get_name()+'的新员工号:'+marvin.get_sn())

# 参考link:
# http://www.cnblogs.com/lovemo1314/archive/2011/05/03/2035005.html
