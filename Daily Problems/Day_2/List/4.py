# 9. Clone or Copy a List

def clone(sample):
    clone = []
    for i in range(len(sample)):
        clone.append(sample[i])
    return clone


sample = [1,2,4,5]

print(clone(sample))