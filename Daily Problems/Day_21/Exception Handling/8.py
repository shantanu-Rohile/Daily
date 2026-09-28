# 8. Handle ArithmeticError Exception in Division

def arith(x):
    try:
        return x/0
    except ArithmeticError:
        print("Arithmatic Error")

arith(10)