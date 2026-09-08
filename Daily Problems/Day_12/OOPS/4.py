# 4. Shape Class with Subclasses for Different Shapes
from abc import ABC,abstractclassmethod
import math
class Shapes(ABC):

    @abstractclassmethod
    def area():
        pass
    @abstractclassmethod
    def perimeter():
        pass
class Circle(Shapes):
    def __init__(self,rad):
        self.rad=rad

    def area(self):
        print(f"Area of circle is : {math.pi*(self.rad)**2}")
    def perimeter(self):
        print(f"Perimeter of circle is : {math.pi*(self.rad)*2}")

class Square(Shapes):
    def __init__(self,side):
        self.side=side

    def area(self):
        print(f"Area of square is : {(self.side)**2}")
    def perimeter(self):
        print(f"Perimeter of square is : {4*(self.side)}")

class Rectangle(Shapes):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print(f"Area of rectangle is : {(self.length)*(self.width)}")
    def perimeter(self):
        print(f"Perimeter of rectangle is : {2*(self.length)+ 2*(self.width)}")

class Triangle(Shapes):
    def __init__(self,base,height,side1,side2,side3):
        self.base=base
        self.height=height
        self.side1=side1
        self.side2=side2
        self.side3=side3

    def area(self):
        print(f"Area of Triangle is : {0.5*(self.base)*(self.height)}")
    def perimeter(self):
        print(f"Perimeter of Triangle is : {(self.side3)+(self.side1)+(self.side2)}")



print("Select the shape")

print("1. Circle")

print("2. Square")

print("3. Rectangle")

print("4. Triangle")

chosen_shape = int(input("Chose serial number representing the shape : "))


if chosen_shape == 1 :
    rad = int(input("give a radius : "))

    c1 = Circle(rad)

    c1.area()

    c1.perimeter()

if chosen_shape == 2 :
    side = int(input("give a side size : "))

    s1 = Square(side)

    s1.area()

    s1.perimeter()

if chosen_shape == 3 :
    length = int(input("give a length : "))

    width = int(input("give a width : "))

    r1 = Rectangle(length,width)

    r1.area()

    r1.perimeter()

if chosen_shape == 4 :
    base = int(input("give a base : "))

    height = int(input("give a height : "))

    side1 = int(input("give a side 1 : "))

    side2 = int(input("give a side 2 : "))

    side3 = int(input("give a side 3 : "))

    t1 = Triangle(base,height,side1,side2,side3)

    t1.area()

    t1.perimeter()