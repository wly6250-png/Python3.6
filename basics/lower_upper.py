# -*- coding: UTF-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)==True]
L3 = [s.lower() if isinstance(s,str) else s for s in L1]
L4 = [s.upper() if isinstance(s,str) is True else s for s in L3]
L5 = [s[:1].upper()+s[1:].lower() if isinstance(s,str) else s for s in L4]
print('L1:',L1)
print('L2:',L2)
print('L3:',L3)
print('L4:',L4)
print('L5:',L5)

# map()实现
def normalize(name):
    return name[:1].upper()+name[1:].lower() 

M1 = ['adam', 'LISA', 'barT']
M2 = list(map(normalize, M1))
print(M2)

# 列表生成式实现
M3 = [s[:1].upper()+s[1:].lower() if isinstance(s,str) else s for s in M1]
print(M3)
