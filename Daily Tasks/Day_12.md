# JVM DAILY TASKS - (Python)

## DAY 12

### 1. **Write a Python program to create a class representing a Circle. ...**
```Python
class Circle:
    def __init__(self,radius):
        self.radius=radius
        self.diameter  = 2*self.radius
    def Area(self):
        return f"Area of Circle : {3.14*self.radius**2}"
    def Circumference(self):
        return 2*3.14*self.radius

c1 = Circle(5)

print(c1.diameter)
print(c1.Area())
print(c1.Circumference())
```

```
10
Area of Circle : 78.5
31.400000000000002
```
### 2. **Write a Python program to create a person class. ...**

```Python
class Person:
    def __init__(self,name,age,gender,profession):
        self.name = name
        self.age = age
        self. gender = gender
        self.profession = profession
    
shantanu = Person("Shantanu Rohile",22,"male","Data Engineer")

sandesh = Person("Sandesh Pasalkar",23,"male","Data Engineer")

print(sandesh.name)

print(shantanu.profession)
    
```

```
Sandesh Pasalkar
Data Engineer
```

### 3. **Write a Python program to create a calculator class. ...**
```Python
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return f"Addition of two numbers is : {self.a + self.b}"
    def sub(self):
        return f"Subtraction of two number is : {self.a - self.b}"
    def mul(self):
        return f"Multiplication of two number is : {self.a * self.b}"
    def devide(self):
        return f"Multiplication of two number is : {self.a / self.b}"

c1= Calculator(10,20)
print(c1.add())
```

```
Addition of two numbers is : 30
```
### 4. **Write a Python program to create a class that represents a shape.**

```Python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(Self):
        pass


class Rectangle(Shape):
    
    def __init__(self,length,width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def area(self):
        return f"Area of {self.name} is : {self.length*self.width}"
        
    def perimeter(self):
        return f"Perimeter of {self.name} : {2*self.length+2*self.width}"
        
        
s1 = Rectangle(8,3)

print(s1.area())

print(s1.perimeter())
```

```
Area of Rectangle is : 24
Perimeter of Rectangle : 22
```

### 5. **Convert two lists into a dictionary**
```Python
lst1 = [1,2,3,4,5]
lst2 = ["red","blue","blue","green","white"]

res = dict(zip(lst1,lst2))

print(res)
```
```
{1: 'red', 2: 'blue', 3: 'blue', 4: 'green', 5: 'white'}
```
### 6. **Merge two Python dictionaries into one**

```Python
dict1 = {1: 'red', 2: 'blue', 3: 'blue', 4: 'green', 5: 'white'}
dict2 = {"orange":12,"Apple":12,"Mangos":24}

res = dict1.update(dict2)

print(dict1)

```

```
{1: 'red', 2: 'blue', 3: 'blue', 4: 'green', 5: 'white', 'orange': 12, 'Apple': 12, 'Mangos': 24}
```
### 7. **Print the value of key ‘history’ from the below dict**

```Python
print(dic1[history])
```

### 8. **Initialize dictionary with default values**

```Python

lst = [1,2,3,4,6,7]

res = dict.fromkeys(lst)

print(res)

```

```
{1: None, 2: None, 3: None, 4: None, 6: None, 7: None}

```
### 9. **Create a dictionary by extracting the keys from a given dictionary**
```Python
orignal = {
    "name" : "sandy",
    "id"   :  35,
    "college" : "RMD Sinhgad"
}

extract = ["college","name"]

new_dict ={}

for i in extract:
    for j in orignal:
        if i==j:
            new_dict.update({i:orignal[i]})
            break
        else:
            new_dict.update({i:"null"})
            

print(new_dict)
```

```
{'college': 'RMD Sinhgad', 'name': 'sandy'}
```
### 10. **Delete a list of keys from a dictionary**

```Python
dict1= {1: 'red', 2: 'blue', 3: 'blue', 4: 'green', 5: 'white', 'orange': 12, 'Apple': 12, 'Mangos': 24}
lst = [1,2,3,4,5]
for i in lst:
    if i in dict1:
        del dict1[i]
        
print(dict1)

```
```
{'orange': 12, 'Apple': 12, 'Mangos': 24}
```
### 11. **Check if a value exists in a dictionary**

```Python
dict1= {1: 'red', 2: 'blue', 3: 'blue', 4: 'green', 5: 'white', 'orange': 12, 'Apple': 12, 'Mangos': 24}
print('Mangos' in dict1)
```

```
True
```

### 12. **Rename key of a dictionary**

```Python
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

my_dict["orange"] = my_dict.pop("banana")

print(my_dict)
```

```
{'apple': 1, 'cherry': 3, 'orange': 2}
```
### 13. **Get the key of a minimum value from the following dictionary**

```Python
lst = {1:"Apple",2:"orange",3:"watermellon"}

min = 10000

for i in lst:
    if i<=min:
        min = i
        
print(min)
```
```
1
```
### 14. **Change value of a key in a nested dictionary**

```Python
dict1 = {1:{2:"whale",3:"dragon"},4:"Tiger"}



dict1[1][5] = dict1[1].pop(3)


print(dict1)
```

```
{1: {2: 'whale', 5: 'dragon'}, 4: 'Tiger'}
```