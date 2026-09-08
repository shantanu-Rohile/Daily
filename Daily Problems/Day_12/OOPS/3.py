# 3. Calculator Class for Basic Arithmetic Operations

class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print("Add : ",self.num1 + self.num2)
    def sub(self):
        print("Subtract : ",self.num1 - self.num2)
    def mul(self):
        print("Multiply : ",self.num1 * self.num2)
    def divide(self):
        print("Division : ",self.num1 / self.num2)
        


num1 = int(input("Enter a number : "))


num2 = int(input("Enter a number : "))

calc = Calculator(num1,num2)

calc.add()
calc.sub()
calc.mul()
calc.divide()
