def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
#a=int(input('please enter the number:'))
#print('the abs is:',my_abs(a))
