# JVM DAILY TASKS - (Python)

## DAY 4


### **1. What are decorators?**

- Decorators are used to modify functions.
- @ is used to modify functions

```Python

def greet(fx):
    def mfx():
        print("Good morning, thanks for using this function")
        print(fx())
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    return "Hello, world!"

hello()
```

```
PS E:\JVM\0-JVM\Python JVM\practice> python3 3.py
Good morning, thanks for using this function
Hello, world!
Thanks for using this function
PS E:\JVM\0-JVM\Python JVM\practice> 
```

### **2. How does break, continue, and pass work?**

- In python break, continue, pass are used to change the standard flow of lopp

- ```break``` stops the entire loop

- ```continue``` skips the remaining code in iteration and jump to next iteration

- ```pass``` does absolutely nothing it works as a syntactical placeholder

```Python

for i in range(100):
    if(i == 3):
        continue
    elif(i == 11):
        break
    else:
        print(i, end = " ")


for i in range(100):
    pass

# for i in range(100):
```

```Python
for i in range(100):
```

```
S E:\JVM\0-JVM\Python JVM\practice> python3 4.py
  File "E:\JVM\0-JVM\Python JVM\practice\4.py", line 15
    for i in range(100):
IndentationError: expected an indented block after 'for' statement on line 15
```

### **3. How to comment with multiple lines in Python?**

- using ''' content '''

### **4. What are Dict and List comprehensions?** 

- Dict and List comprehensions are method of creating dict and list in short and simple manner

```Python
list= [i*i for i in range (1,11) ]

print(list)

new_list= [i*i for i in range (1,11) if i % 2 == 0 ]

print(new_list)


new_dict = {i:i*i for i in range(1,11)}

print(new_dict)
```

```
PS E:\JVM\0-JVM\Python JVM\practice> python 5.py
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[4, 16, 36, 64, 100]
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
PS E:\JVM\0-JVM\Python JVM\practice> 
```

### **5. What is the difference between range & xrange?**

- xrange() was in python2 but it is now removed from python3
- xrange() and range() are diffrence in the python2
    - xrange() generated numbers lazily one at a time
    - range() use to generate entire of list of numbers in memory
- but in python3 range() works exactly like xrange() from python2
 
### **6. How will you remove duplicate elements from a list?**
- By using set function

```Python
li = [1,2,3,4,5,6,7,7,6,8,8,9,1,2,3,4,5,6,7,8,9]

print(li)

li = list(set(li))

print(li)
```

```
PS E:\JVM\0-JVM\Python JVM\practice> python3 6.py
PS E:\JVM\0-JVM\Python JVM\practice> python3 6.py
[1, 2, 3, 4, 5, 6, 7, 7, 6, 8, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### **7. How will you read a random line in a file?**

```Python

# Print random line from the code
import random


with open("assets/test.txt","r") as file:
    lines = file.readlines()
    random_line = random.choice(lines)
    print(random_line)

```

```
PS E:\JVM\0-JVM\Python JVM\practice> python3 7.py
Kuoh Academy remains peaceful for approximately seven minutes.
```

### **8. Write a Python program to count the total number of lines in a text file?**


```Python
# Total number of lines of text in file

with open("assets/test.txt","r") as file:
    data = file.read()
    lines = data.splitlines()
    print("Total number of lines in file:", len(lines))

```

```
PS E:\JVM\0-JVM\Python JVM\practice> python3 8.py
Total number of lines in file: 7
PS E:\JVM\0-JVM\Python JVM\practice> 
```