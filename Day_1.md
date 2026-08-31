# JVM DAILY TASKS - >

## DAY 1

### **Q1. What is Python?**

Python is a general purpose programming Langrage. It is programming language with easy to use English like syntax. Python is widely used in field of data due to libraries offered by python. 


### **Q2. Python is an interpreted language. Explain**

Python, Java, C++, C are not the native languages of computer, computer only understands the binary/machine language i.e. (0 and 1's).
0 - no current
1 - current
 
step 1 : Writing code in IDE (integrated development environment) 

step 2 : Saving the file (name.py : Source File)

step 3 : Source file is then sent to the compiler. Compiler converts the python code into the byte code (name.pyc). Byte code is not 	 understood by the computer.

step 4 : The byte code is then sent to the python environment machine where it is then converted into machine code.

step 5 : Machine code is sent to the computer it process it and then send result.


### **Q3. What is the difference between lists and tuples?**

- Lists are mutable but tuples are not
- Tuples ()
- Lists []
- Lists can not be used as dictionary keys but we can use Tuples as dictionary key.


### **Q4. What is pep 8?** 

- pep8 stands for Python Enhancement Proposal 8 
    1. use 4 spaces for indentation 

    ```Python
    def sum(a,b):
        return a + b
    ```

    2. Keep lines under 79 characters
    ```Python
    result = some_function(
        argument_one,
        argument_two,
        argument_three,
        argument_four,
        argument_five,
    )
    ```
    3. Follow namming Convention
        - Variables : sanke_case : user_name
        - Functions : snake_case : calculate_total()
        - Classes   : PascalCase : BankAccount
        - Constants : UPPER_CASE : MAX_SIZE
        - Modules   : sanke Case : file_utils.py

    4. Add spaces around operators

    ```Python 
    x = a + b
    ```

    5. Use blank lines to separate code

    ```Python
    def sum(a, b):
        return a + b
        
    def mul(a, b):
        return a * b

    ```

    6. Import Modules Cleanly

    ```Python

    import pandas as pd
    import numpy as np

    ```

    7. Compare to None using is

    ```Python 

    if value is None:

    ```

    8. Write descriptive names

### **Q5. What are the Key features of Python?**

1. Easy to Learn and Read

2. Interpreted Language

3. High-Level Language
    - It abstracts lo-level details like memory managment, allowing developers to focus on problem solving.

4. Object-Oriented

5. Cross-Platform (can run on windows, linux, mac)

6. Large Standard Library

7. Open Source and Free

8. Dymnamic Typping 
    - Variables do not need explicit data type declaration 
    - Types are declared automatically at runtime

9. Python use automatic Garbage collection to managage memory, reducing the likelyhood of memeory leaks.

10. Extensible and Embeddable

11. Versatile Applications

### **Q6. How is Memory managed in Python?**


### **Q7. What is PYTHONPATH?**

- PYTHONPATH is an enviroment variable that tells Python where to look for modules and packages when you use import.

### **Q8. What are Python Modules?**

- Python modules is simply a Python File ```(.py)``` containing code that can be resused in another python program. 

### **Q9. What are python namespaces?**
### **Q10.garbage collector?**
- The garbage collector (GC) is a part of Python that automatically finds and removes objects from memory that are no longer being used.