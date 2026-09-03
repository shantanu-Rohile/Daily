# 33. Print integers with left-padded zeros.

def func(num):
    num = str(num)
    list1= []
    for i in range(len(num)):
        list1.append("0")

    res = "".join(list1)
    return res+num

print(func(42))