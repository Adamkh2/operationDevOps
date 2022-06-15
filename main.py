import sys
def addition(a, b):
    return a + b

def multiplication(a,b):
    return a * b 

def soustraction(a,b):
    return a - b

def division(a,b):
    if (b==0): 
        return -1
    return a / b


x = 34
y = 2

if (division(x,y)!= -1):
    print('division possible')
else:
    print('division impossible')

