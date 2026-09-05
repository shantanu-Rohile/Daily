# 1. Triple Numbers Map

def triple_number(sample):
    res = list(map((lambda x : x*3),sample))
    return res

print(triple_number([1,2,3,4,5,6]))
