# 4. Validate Numerical Inputs and Raise TypeError

def add(x,y):
    return x+y

try:
    add(100,'1000')
except Exception as e:
    print(e)
    print('Input only Integers')