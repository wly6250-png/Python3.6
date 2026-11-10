def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    print('numbers:',numbers)
    return sum
