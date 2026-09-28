# 1. Handle ZeroDivisionError Exception

def func(x):
    return x/0

try:
    func(10)
except ZeroDivisionError:
    print("Can not devide the number by zero")
