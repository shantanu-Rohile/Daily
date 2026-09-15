# 10. Queue Data Structure Class

class Quee:
    def __init__(self):
        self.quee = []

    def display(self):
        for i in self.quee:
            print(i,"->",end=" ")
        print("null")
    
    def push(self,value):
        if len(self.quee) == 0:
            self.quee.append(value)
            self.display()
        else:
            self.quee.insert(0,value)
            self.display()
    def pop(self):
        length = len(self.quee)
        self.quee.pop(length-1)
        self.display()


q1 = Quee()

q1.push(1)

q1.push(10)

q1.push(100)

q1.push(1000)

q1.push(10000)

q1.pop()