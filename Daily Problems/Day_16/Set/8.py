# 8. Create Set Difference

def diff(set1,set2):
    res = set()
    for i in set1:
       if i not in set2:
           res.append(i)

    return res


set1 = {1,2,3,4,5}

set2 ={3,4,5,6,7}

print(diff(set1,set2))