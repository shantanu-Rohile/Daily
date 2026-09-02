# 27. Find Second Smallest Number in List
def second_smallest(list1):
    second_min= 1000000
    mini = min(list1)
    for i in range(len(list1)):
        if list1[i]<second_min and list1[i] != mini :
            second_min=list1[i]

    return second_min


list1=[1,2,3,4]
print(second_smallest(list1))