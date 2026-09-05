# 7. List Addition and Difference Map

def add_diff(sample1,sample2):
    res = list(map(lambda x,y: (x+y,x-y),sample1,sample2))
    return res

print(add_diff([1,2,3,4],[3123,3123,43241]))