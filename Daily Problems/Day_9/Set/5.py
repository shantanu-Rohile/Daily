# 15. Find the Length of a Set

def length(sample):
    length = 0
    for i in sample:
        length += 1
    return length


sample = {1,2,3,4,5}
print(length(sample)) 