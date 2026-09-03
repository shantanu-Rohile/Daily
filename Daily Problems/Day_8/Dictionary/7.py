# 7. Create a Union of Sets

def union_of_set(sample1,sample2):
    # res = sample1.union(sample2)

    res = sample1.copy()
    for i in sample1:
        for j in sample2:
            if i != j :
                res.add(j)

    return res

sample1 = {1,2,3,4,5,6,7}

sample2 = {3,4,5,6,7,8,9}

print(union_of_set(sample1,sample2))
