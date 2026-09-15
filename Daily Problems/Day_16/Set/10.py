# 10. Check if a Set is a Subset of Another Set

def is_subset(set1,set2):
    for i in set1:
        if i not in set2:
            return("set1 is not subset of set2")

    return("set1 is subset of set2")

set1 = {4,5}

set2 ={3,4,5,6,7}

print(is_subset(set1,set2))