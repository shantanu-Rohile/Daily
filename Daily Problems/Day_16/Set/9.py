# 9. Create a Symmetric Difference

def symme_diff(set1,set2):
    res = set()
    for i in set1:
        if i not in set2:
            res.add(i)
    for i in set2:
        if i not in set1:
            res.add(i)

    return res

set1 = {1,2,3,4,5}

set2 ={3,4,5,6,7}

print(symme_diff(set1,set2))