# 15. Get Maximum and Minimum Values of a Dictionary

def min_max_dict(sample):
    res=sorted(sample.items(),key = lambda x: x[1])
    return res[0], res[-1]


sample = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(min_max_dict(sample))