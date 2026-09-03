# 6. Create an Intersection of Sets

def intersection(sample1,sample2):
    # res= sample1.intersection(sample2)
    res = set()
    for i in sample1:
        for j in sample2:
            if i == j :
                res.add(i)
    return res

sample1 = {1,2,3,4,5,6,7}

sample2 = {3,4,5,6,7,8,9}

print(intersection(sample1,sample2))