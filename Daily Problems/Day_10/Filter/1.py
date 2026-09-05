# 1. Even Number Filter

def even(num):
    even=list(filter(lambda x : x%2==0,num))
    return even


print(even([1,2,3,4,5,6,8,10,12]))