# 37. Find Common Items in Lists

def common_tems(lst1,lst2):
    res = []
    for i in lst1:
        if i in lst2:
            res.append(i)

    print(res)


lst1 = [1,2,3,4,5,6,7,8]

lst2 = [1,2,3,4,10,11,12,12,13,12,15]

common_tems(lst1,lst2)