# 29. Get Unique Values from List

def unique_number(list1):
    res = []
    for i in list1:
        if i in res:
            continue
        else:
            res.append(i)
    return res


list1 = [1,22,33,4,2,33,44,33,22,2,4,5,66,4,55,55,777,666,66,77,666,777]

print(unique_number(list1))