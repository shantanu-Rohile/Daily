# 8. Create Set Difference

def diffrence(set1,set2):
    res = set1.difference(set2)

    return res

set1 = {1,2,3,4,5,6,7}

set2 = {3,4,5,6,7,8,9,10} 

print(diffrence(set1,set2))