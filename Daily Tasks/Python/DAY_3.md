# JVM DAILY TASKS - (Python)

## DAY 3


### 1. **what is bytearray?**

- bytearray() is built-in data type of python that stores a mutable sequence of integers ranging from 0 to 255

- byte and bytearray bot store the raw data

```Python
a = bytearray('hey, good morning !', "utf-8")

print(a)

print("before cahnge : ",id(a))

a[1]= 105

print("after cahnge : ",id(a))

```

```
bytearray(b'hey, good morning !')
before cahnge :  1868314150832
after cahnge :  1868314150832
```

### 2. **difference between byte and bytearray?**

- byte is immutable and bytearray is mutable

```Python
a = bytes('hey, good morning !', "utf-8")

print(a)

a[1]= 105

print(a)

```

```
b'hey, good morning !'
Traceback (most recent call last):
  File "C:/Users/ca220/OneDrive/Documents/Python Practice/byte_bytearray.py", line 5, in <module>
    a[1]= 105
TypeError: 'bytes' object does not support item assignment
```


### 3. **what is indexing?**

- Indexing means accessing the element in sequnced data using position.

### 4. **explain  about slicing?**

- Slicing means not accessing only single element at oen position but sequence of elements
- ``` slicing[start:end:step] ```

```Python
list=[1,2,3,5,6,7,8,12,342,43545,000,6456,5245245,45232525,5235325235,523523523523525,3223,435235,21313,7467467,58658]

print(list[1:len(list):2])
```

```
[2, 5, 7, 12, 43545, 6456, 45232525, 523523523523525, 435235, 7467467]
```

### 5. **how can we do reverse slicing?**

- reverse sclicing is similar to sclicing but reversing the sequence

- ``` slicing[start:end:step] ```

```Python

list=[1,2,3,5,6,7,8,12,342,43545,000,6456,5245245,45232525,5235325235,523523523523525,3223,435235,21313,7467467,58658]

print(list[len(list):0:-2])

```

```
[58658, 21313, 3223, 5235325235, 5245245, 0, 342, 8, 6, 3]
```

### 6. **explain about assert statement?**

- assert is used to whether the condition is true, if it is false we receive AssertError
- It's used in debugging and developing

### 7. **what is array?**

- In programming language array is a data structure that stores multiple values of same data type in sequential manner, where as values are stored in contiguous memory locations.

### 8. **what are the local variable?**

- Local variable is variable created inside the function and you can access that variable only inside that function

### 9. **what is global variable?**

- Global variable is accessible throughout the global scope
- you can use global variable throughout the module, it bound to global namespace

### 10. **what are the mutable and immutable object?**

- Content of mutable objects can be changed after creation 
- Contents of immutable objects can not be changed after creation

```Python


a = [1,2,34,5,6]

print("id before change : ", id(a))

a[2]=3

print("id After change : ", id(a))



a = (1,2,34,5,6)

print("id before change : ", id(a))

a[2]=3

print("id After change : ", id(a))


```

```
id before change :  1482793545600
id After change :  1482793545600
id before change :  1482838017408
Traceback (most recent call last):
  File "C:/Users/ca220/OneDrive/Documents/Python Practice/mutable_immutable.py", line 17, in <module>
    a[2]=3
TypeError: 'tuple' object does not support item assignment
```