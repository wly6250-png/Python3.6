# -*- coding: utf-8 -*-
# 规律为——阳干配阳支，阴干配阴支;
a = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
b = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
c=[]
for i,t in enumerate(a):
    for j,d in enumerate(b):
        if i%2==0:
            if j%2==0:
                c.append(t+d)
        else:
            if j%2==1:
                c.append(t + d)
print(c)
