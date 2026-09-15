# 1. Create a Set

s1 = [1,2,3,4,5,5,6,6,6,6,1,2,3,4]

set1 = []

for i in s1:
    if i in set1:
        pass
    else:
        set1.append(i)

print(set1)