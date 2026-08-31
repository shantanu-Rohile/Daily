# 16. Generate Square Numbers in Range

def sq_number():
    list1=[]
    list2=[]
    for i in range(1,6):
        list1.append(i**2)
    for i in range(25,31):
            list2.append(i**2)

    return list1, list2

print(sq_number())
    