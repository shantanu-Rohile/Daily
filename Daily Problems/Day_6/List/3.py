# 28. Find Second Largest Number in List

def second_largest(list1):
    largest = max(list1)
    second_largest = -10000
    for i in list1:
        if i > second_largest and i != largest :
            second_largest = i
    return second_largest

list1 = [1,2,3,4,5,0,11]

print(second_largest(list1))