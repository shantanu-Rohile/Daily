# JVM DAILY TASKS - (Python)

## DAY 5

slicing

### 1. **str="welcome to my blog"**

```Python
str="welcome to my blog"


print("1 : ",str[3:18])
print("2 : ",str[2:14:2])
print("3 : ",str[:7])
print("4 : " ,str[-9:-15]) # Here we are getting empty string because we have not added :-1 as step therefore python still takes +1 step
print("4 : " ,str[-9:-15:-1])
print("5 : " ,str[8:25:3])
print("6 : " ,str[0:9:3])

print(len(str))

```

```
PS E:\JVM\0-JVM\Python JVM\practice> python3 17.py
1 :  come to my blog
2 :  loet y
3 :  welcome
4 :  
4 :  ot emo
5 :  tmbg
6 :  wce
18
PS E:\JVM\0-JVM\Python JVM\practice> 
```

### 2. **what are the features of python?**

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

### 3. **what are the logical operator?**

- Logical operators are the operators that show realtionship between two conditions
- ( ```and``` , ```or``` , ```not``` ) are the logical operators in python
- ```and``` : 
    - if both conditions are true then then result is also true
    - if any one condition is false result is false
    - if bot are false result is false

- ```or```  : if both conditions are false then only result is false in other cases result is true

- ```not``` : reverse the result. If result is true then it will be convereted to false, and if result is false then it is covreted to true.

### 4. **what are boolean operator?**

- LOgical operators are also known as boolean operators

### 5.**enter 3 number and find their sum and average?**

```Python
# enter 3 number and find their sum and average?

num1 = int(input("Add first number : "))

num2 = int(input("Add Second number : "))

num3 = int(input("Add third number : "))

num = [num1,num2, num3]

print("Sum of numbers : ",sum(num))


print("Average of numbers : ",sum(num)/len(num))
```

```
PS E:\JVM\0-JVM\Python JVM\practice> python3 18.py
Add first number : 10
Add Second number : 20
Add third number : 30
Sum of numbers :  60
Average of numbers :  20.0
PS E:\JVM\0-JVM\Python JVM\practice> 
```


