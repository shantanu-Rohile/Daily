# 17. Unzip a List of Tuples into Individual Lists

def unzip(sample):
    res = []
    for i in range(len(sample)):
        res.append(list(sample[i]))
    return res

sample = [(1,2),(3,4),(5,6),(7,8)]

print(unzip(sample))
    