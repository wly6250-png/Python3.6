# -*- coding: utf-8 -*-
def volid(pwd):
    p = bool(pwd)  #判断是否为空，为空则返回False
    e = bool(6<=len(pwd)<=10)
    a = any(map(str.isupper,pwd))
    b = any(map(str.islower,pwd))
    c = any(map(str.isdigit,pwd))
    d = not all(map(str.isalnum,pwd))
    return all([p,e,a,b,c,d])
PW=input('please enter your password:')
print('check result is:',volid(PW))
