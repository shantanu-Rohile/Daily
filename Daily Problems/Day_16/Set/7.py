# 7. Create a Union of Sets

# 6. Create an Intersection of Sets

def union(set1,set2):
    res = set()
    for i in set1:
        if i not in res:
            res.add(i)

    for i in set2:
        if i not in res:
            res.add(i)

    return res


set1 = {1,2,3,4,5}

set2 ={3,4,5,6,7}

print(union(set1,set2))