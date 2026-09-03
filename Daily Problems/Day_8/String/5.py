# 35. Display number with comma separator.

def func(num):
    num = str(num)
    list1= []
    for i in range(len(num)):
        list1.append(num[i])

    res = ",".join(list1)
    return res

print(func(43242))