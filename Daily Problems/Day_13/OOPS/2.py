# 6. Stack Data Structure Class

class Stack:

    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.insert(0,value)
    def pop(self):
        self.stack.pop(0)
    def display(self):
        print(self.stack)



s1 = Stack()

s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)

s1.display()

s1.pop()

s1.display()

