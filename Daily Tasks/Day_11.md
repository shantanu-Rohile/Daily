# JVM DAILY TASKS - (Python)

## DAY 11

### 1. **Explain Inheritance with an example?**

- Child class inheriting the properties of parent class

```Python
class Mamals:
    def __init__(self,sound,diet):
        self.sound=sound
        self.diet= diet
        self.group="mamals"
        self.reproduction= "By giving birth"
    
    def info(self):
        print(f"sound : {self.sound}")
        print(f"diet : {self.diet}")
        print(f"group : {self.group}")
        print(f"reproduction : {self.reproduction}")
        
        
class Dog(Mamals):
    
    def __init__(self):
        super().__init__("bark","omnivorous")
        


d1 = Dog()


d1.info()
```

```
sound : bark
diet : omnivorous
group : mamals
reproduction : By giving birth
```
### 2. **What is a copy constructor?**

- Copy constructor is constructor used to create new copy of exeisting object of same class
- python do not have copy constructor butwe can create a new copy of object using copy() key word
### 3. **What is a destructor?**

- destructor is a function that is automatically called when object is destryed or goes out of scope

- to free memory and other resources

- you can do it manually in c++

- in python we have garbage collector for same

### 4. **What are the various types of inheritance?**

- Single level inheritance :
    - A child class inherite from parent class
- Multilevel Inheritance :
    - A child class inherite from another child class creating a chain
-  Hierarchical Inheritance :
    - Multiple child claases inherite from one parent class
- Multiple Inheritance :
    -  A child class inherite from multiple parent classes

    
### 5. **What is a subclass?**

- A class that inherte's the methods and properties of other class is called subclass

6.Define a superclass?

- A class from which subclass inherits the methods and properties is called superclass

### 7. **What is meant by static polymorphism?**

- In static polymorphism the method to run is decided before execution of program

### 8. **What is meant by dynamic polymorphism?**

- In dynamic polymorphism the method to run is decided during execution of program

### 9. **What is the difference between overloading and overriding?**

- Method Overloading:

    1. Method overloading means that program have methods with similar names (hence the ***over***laoding) and compiler choose the method to run based on parameters .

    2. chosen by compiler means before running the program. I.e method overlaoding is associated with static polymorphism.

- Method Overriding : 

    1. Method overriding means overriding the behaviour of parent class by child class

    2.  Method overriding is associated with dynamic polymorphism.

### 10. **What is an abstract class?**

- Abstract class strictly works as a blue print and no object can be created for this class

- Other child classes can inherit it and will have to implement all methods in the said class

- Abstract classes can contain both abstract methods (empty blueprints) and concrete methods (fully implemented code)

### 11. **What is an exception?**

- Exception is an abnormal or abrupt event that occurs during execution of program and interupts the flow of program

### 12. **What is meant by exception handling?**

- Exception handling is a programming process used to respond to unexpected runtime errors, preventing a program from crashing abruptly