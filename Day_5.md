# JVM DAILY TASKS - (Python)

## DAY 5

### 1: **Add a list of elements to a set**

```Python

main_set = set('abc')

list_set = ['d','e','f']

main_set.update(list_set)

print(main_set)

```

```
PS E:\JVM\0-JVM\Python JVM\Practice> python 9.py
{'e', 'c', 'f', 'b', 'a', 'd'}
PS E:\JVM\0-JVM\Python JVM\Practice> 


```

### 2: **Return a new set of identical items from two sets**

- We use ```copy()``` Function to create a copy of orignal set
- and reason why we can't just do this ``` new_set = main_set ``` is that because although you are creating a new variable but at the end your new ``` new_Set ``` is also pointing towards the same object.

```Python
a = {1, 2, 3}

print("Orignal a : ",a)

b = a

b.add(4)

print("After appending 4 into b : ",a)

c = a.copy()

c.add(5)

print("After appending 5 into c : ",a)
```

```
PS E:\JVM\0-JVM\Python JVM\Practice> python 10.py
Orignal a :  {1, 2, 3}
After appending 4 into b :  {1, 2, 3, 4}
After appending 5 into c :  {1, 2, 3, 4}
PS E:\JVM\0-JVM\Python JVM\Practice> 
```

### 3: **Get Only unique items from two sets**

- To get the elements of bot first and second set excluding duplicate values we have to use the union```(|)```

```Python
a = {1,2,3,4}

b = {3,4,5,6,7,8}

c = a | b

print(c)

c.add(9)

print(c)
```

```
PS E:\JVM\0-JVM\Python JVM\Practice> python 11.py
{1, 2, 3, 4, 5, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
PS E:\JVM\0-JVM\Python JVM\Practice> 
```

- Note : This Union function is similar to the unuion we in set's in mathamatics

![Union](Assets/union.png)

### 4: **Update the first set with items that don’t exist in the second set**
### 5: **Remove items from the set at once**
### 6: **Return a set of elements present in Set A or B, but not both**
### 7: **check if two sets have any elements in common. If yes, display the common elements**
### 8: **Update set1 by adding items from set2, except common items**
### 9: **Remove items from set1 that are not common to both set1 and set2**