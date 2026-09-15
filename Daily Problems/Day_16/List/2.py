# Swap Every n-th and (n+1)th Values

def swap(lst1):
    for i in range(0,len(lst1)-1,2):
        ele1= lst1[i]
        lst1[i] = lst1[i+1]
        lst1[i+1] = ele1

    return lst1

lst = [1,2,3,4,5,611,13,14,15]

print(swap(lst))