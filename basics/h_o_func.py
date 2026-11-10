# -*- coding: utf-8 -*-
# 高阶函数
# 传入函数

def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs))

# 把函数作为参数传入，这样的函数称为高阶函数，
# 函数式编程就是指这种高度抽象的编程范式。
#--------------------------------------------------
# 引入数学模块中的方法
from math import sqrt
from math import tan

# 高阶函数应用，返回一个数字不同方法计算结果
def same(num, *kw):
    # 参数检查
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')

    # 初始化结果字典
    rel = {}
    # 循环计算可变参数
    for func in kw:
        try:
#            rel[str(func)[str(func).find('function ') + 9: -1]] = func(num)
            rel[func.__name__] = func(num)
        except ValueError:
#            rel[str(func)[str(func).find('function ') + 9: -1]] = 'None'
            rel[func.__name__]  = 'None'
    # 返回结果字典
    return rel

# 函数调用
result = same(-10.5, sqrt, abs, tan)
# 结果输出
print(result)

# print(sum) //返回字符串内容:
# <built-in function sum>
# str(sum)   // 返回:
# '<built-in function sum>'
# 1 所以首先要从str(sum发)返回的字符串查找'function '匹配
#   str(sum).find('function ')  //这个返回是10, 意思是:
#   f位于字符串 '<built-in function sum>'中的第10个字符(编号从0开始计算)
# 2 找到function后,要偏移字符串'function '的长度(长度是9)到字符串中sum的字符s所在位置,
#   str(sum).find('function ') + 9 //这个就是s在字符串的位置,假设为p.
# 3 运用之前的切片理论, 从s开始到倒数第一个为止打印出来,即只显示sum.
#   假设s='<built-in function sum>', p就是上面的s在字串的位置,那命令就是:
#   s[p:-1] //从第p个字符开始,输出到倒数第一个为止, 那就是输出sum
# 4 基于第三步骤s[p:-1], 我们采用代入法:
#    s字符串的内容就是从str(sum)获得,所以s=str(sum);
#    p就是步骤1,2描述的函数sum的第一个字符的偏移,所以
#    p=str(sum).find('function ') + 9.
#    代入s[p:-1] 得到:
#    str(sum)[str(sum).find('function ') + 9 : -1]
#    这就是等于从字符串'<built-in function sum>'中只输出sum,即函数名.
