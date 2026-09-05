# 2. Add Three Lists Map Lambda

def add_three_lists(sample1,sample2,sample3):
    res = list(map((lambda x,y,z: x+y+z), sample1,sample2,sample3))

    return res

print(add_three_lists([1,2,3],[4,5,6],[7,8,9]))