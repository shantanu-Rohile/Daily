# 22. Remove Empty Tuple(s) from a List of Tuples

def remove_empty(sample):
    res = sample.copy()
    for i in range(len(sample)):
        if type(sample[i]) == type(()):
            if len(sample[i]) == 0 :
                res.remove(sample[i])
    return res

sample = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

print(remove_empty(sample))