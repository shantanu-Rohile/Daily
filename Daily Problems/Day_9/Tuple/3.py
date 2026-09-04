# 18. Reverse a Tuple

def reverse(sample):
    rev =[]
    for i in range(len(sample)-1,0,-1):
        rev.append(sample[i])

    return tuple(rev)

sample = (1,2,3,4,5,6)

print(reverse(sample))