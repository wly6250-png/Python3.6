# -*- coding: utf-8 -*-
n1=255
n2=1000
n3=12.34
n4='你好'
n5='ABC'
print(n1,'的十六进制是:',hex(n1))
print(n2,'的十六进制是:',hex(n2))

print('%d的十六进制是:%s \n%d的十六进制是:%s'%(n1,hex(n1),n2,hex(n2)))
print('0x%x,0x%x'%(n1,n2))

print(n3,'的十六进制是:',float.hex(n3))
import binascii
print(n4,'的十六进制是:',binascii.b2a_hex(n4.encode("utf8")))
print(n5,'的十六进制是:',binascii.b2a_hex(n5.encode("utf8")))
