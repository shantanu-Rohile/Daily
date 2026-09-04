# 14. Find Maximum and Minimum Values in a Set

def min_max(sample):
    max = -1000
    min = 1000

    for i in sample:
        if i > max:
            max = i

        if i < min:
            min = i 

    return max,min

sample = [1,2,3,4,5,6,7,8]

print(min_max(sample))