# 34. Print integers with * right-padded.

def func(num):
    num = str(num)
    list1= []
    for i in range(len(num)):
        list1.append("*")

    res = "".join(list1)
    return num+res

print(func(42))