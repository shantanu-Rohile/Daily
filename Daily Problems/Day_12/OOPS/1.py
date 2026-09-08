# 1. Circle Class for Area and Perimeter
import math
class Circle:
    def __init__(self,rad):
        self.rad=rad

    def area(self):
        print(f"Area of circle is : {math.pi*(self.rad)**2}")
    def perimeter(self):
        print(f"Perimeter of circle is : {math.pi*(self.rad)*2}")


c1 = Circle(10)

c1.area()