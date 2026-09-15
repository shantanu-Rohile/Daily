# 6. Create an Intersection of Sets

def intersect(set1,set2):
    res = set()
    for i in set1:
        if i in set2:
            res.add(i)

    return res

set1 = {1,2,3,4,5}

set2 ={3,4,5,6,7}

print(intersect(set1,set2))