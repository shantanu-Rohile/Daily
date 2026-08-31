# JVM DAILY TASKS - (Python)

## DAY 7


### 1. **what is range data type?**

- Range data type is used to calculate total numer of elements in the data type and is used to iterate 

### 2. **what is user defined datatype?**

- As everything in python is object, user defined datatype is data type created by user 
- Example
    ```Python
    class Point:

        def __init__(self,x:float,y:float):
            self.x =x
            self.y=y


    p1 = Point(10.0,20.0)

    print(type(p1))
    ```

    ```
        PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 19.py 
        <class '__main__.Point'>
        PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> 
    ```

### 3. **what are the control statement?**

- Control statement are the one's who control the flow of program
- ex : ``` if ``` , ```else``` and ```elif```

4. explain with one example each

- if statement

    - if statement is used to execute a block of code when a condition is True.

    ```Python

    age = 20

    if age >= 18:
        print("Eligible to vote")
    ```
    ```
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 21.py
    Eligible to vote
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious>
    ```

- if ..else statement

    - if..else executes one block when the condition is True and another when it is False.

    ```Python

    num = 15

    if num % 2 == 0:
        print("number is even")
    else:
        print("number is odd")
    ```

    ```
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 22.py
    number is odd
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious>
    ```

- while loop

    - while loop repeatedly executes code while a condition is True.

    ```Python

    i = 1

    while i <= 5:
        print(i, end=" ")
        i += 1
    ```
    ```
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 23.py
    1 2 3 4 5
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious>
    ```

- for loop

    - for loop is used to iterate over a sequence or range.

    ```Python

    for i in range(1, 6):
        print(i, end=" ")
    ```

    ```
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 24.py
    1 2 3 4 5
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious>
    ```

- break statement

    - break immediately terminates the loop.

    ```Python

    for i in range(1, 11):
        if i == 6:
            break
        print(i, end=" ")

    ```

    ```

    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 25.py
    1 2 3 4 5
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious>

    ```

- continue statement

    - continue skips the current iteration and moves to the next one.

    ```Python

    for i in range(1, 11):
        if i == 6:
            continue
        print(i, end=" ")

    ```
    ```
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 26.py
    1 2 3 4 5 7 8 9 10
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious>
    ```

- pass statement

    - pass does nothing and is used when a statement is required syntactically.

    ```Python

    num = 10

    if num > 5:
        pass

    print("Program completed")

    ```
    ```
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 27.py
    Program completed
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious>
    ```

- return statement :

    - return is used inside a function to send a value back to the caller.

    ```Python
    def add(a, b):
        return a + b

    result = add(10, 20)
    print(result)
    ```

    ```
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 28.py
    30
    PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious>
    ```
            
### 5. **write a program to find even number?**

 ```python
def is_even_number(num):
    if num % 2 ==0 :
        print("number is edven")
    else :
        print("number is odd")


is_even_number(1227498714)
```
```
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 20.py
number is edven
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> 

```

### 6. **write a program to find odd number?**
 ```python
def is_even_number(num):
    if num % 2 ==0 :
        print("number is even")
    else :
        print("number is odd")


is_even_number(1227498711)
```
```
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 20.py
number is odd
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> 

```
### 7. **display number from 1 to 10.**
```Python
for i in range(1,11):
    print(i,end=" ")
```
```
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 20.py
1 2 3 4 5 6 7 8 9 10
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> 
```
### 8. **display number from 100-110**
```Python
for i in range(100,110):
    print(i,end=" ")
```
```
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 20.py
100 101 102 103 104 105 106 107 108 109 
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> 
```
### 9. **display even number from 100-110**
```Python
for i in range(100,110):
    if i % 2 ==0 :
        print(i,end=" ")
```

```
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 20.py
100 102 104 106 108 
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> 
```
### 10. **display odd number from 100-110.**
```Python
for i in range(100,110):
    if i % 2 !=0 :
        print(i,end=" ")
```
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> python3 20.py
101 103 105 107 109 
PS E:\JVM\0-JVM\Python JVM\Practice\Misllenious> 

```