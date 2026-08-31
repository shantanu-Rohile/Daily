# JVM DAILY TASKS - >

## DAY 2


### 1. **What is the difference between Python Arrays and lists?**

1. 
    - Lists are built-in python data structures that can store values with diffrent data type.
    - Arrays are no built-in data structures like list, we have to import module to work with arrays.

2. 
    - You can store values with diffrent data type in same list.
    - you can not store values with diffrent data types in same array.

3. 
    - List have lower speed and high memory consumption.
    - Arrays have high computing speed and low memory consumption.

### Note : Why Arrays are faster and show low memory consumption than List ? 

- What Lists looks like  ->
    - numbers = [10, 20, 30, 40]
    - A python list is essentially a references (Pointers) to Python Objects. Because as we know know everything in python is object.
    '''
            numbers
        │
        ▼
        ┌────────┬────────┬────────┬────────┐
        │   ●    │   ●    │   ●    │   ●    │
        └───┼────┴───┼────┴───┼────┴───┼────┘
            │        │        │        │
            ▼        ▼        ▼        ▼
        10       20       30       40
    '''
    - so lists itself does not contain any integers but refrences to the objects.
    - And each python is itself object with extra data attached to it.
- why does Python do this?
    - because in list we are storing data of diffrent sizes. i.e object containing int data has different data size that object containing string data type we store data of equal size in list,arrays so that it becomes easier to navigate for computer when we type list[i] or arr[i] and for same reason we can not directly store objects in list and store references (pointers) of similar data size. 
    - And we store data in objects because python is dynamicaly types so we dont mention data types in python.

- And this creates high memory overhead.
    ```
        10 million list references
        +
        10 million Python integer objects
        +
        metadata associated with those objects
    ```

- But in arrays in python do not store data in objects or the refrences for that matter.




### 2. **what is set?**

- Mathamatically set is collection of distinct elements.
- And in Python set is collection of unique values.
- Set is built-in data structure in python

### 3. **what is frozen set?**

- Frozen set is just immutable and hashable version of set.
- hashable - can be used as key in dictionary and as value in another set

### 4. **what is byte?**

- Byte is unit of digital information that is equals to 8 bit.
- bit is smallest unit of data in computer.

### 5. **difference between set and frozen set?**

- set is mutable and unhashable while the frozen set is imutable and hashable

### 6. **why variables are not declared in python?**

- Because pyhton is dynamically typed language.

### Note : How does this works at lower level 
- suppose ``` x = 10 ``` then you are not storing the 10 in x but refrence (pointer)that refers to object that contains the data type of x and actual data
   ```Python Object

        x
        │
        ▼
        ┌────────────────────┐
        │ Python object      │
        │                    │
        │ type → int         │
        │ value → 10         │
        └────────────────────┘
   ```
- Python's interpreter/runtime is programmed to recognize literals like 10 as integers, create an int object for them, and store the value inside that object.

### 7. **what is sequence?**

- Order of Colelction of items

### 8. **what is mapping?**

- Connecting one element with other elements or element

### 9. **what is dictionary?**

- dictionary is built-in data structure in python that store key value pair.

```Python

stu = {"name":"Shantanu Rohile",
       "staus":"2026 passout",
       "gpa":7.5
       }

print(stu.get("name"))

```

```

========
Shantanu Rohile

```

### 10. **what is range?**

- range() is function in python which is used to control loops.

```Python

for i in range(0,5):
    print(i)


```

```

```Output

 ==========
0
1
2
3
4


```