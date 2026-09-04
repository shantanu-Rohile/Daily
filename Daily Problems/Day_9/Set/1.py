# 11. Create a Shallow Copy of a Set

def shallow_copy(sample):
    res = set()
    for i in sample:
        res.add(i)
    return res

sample = {1,2,3}

print(shallow_copy(sample))
