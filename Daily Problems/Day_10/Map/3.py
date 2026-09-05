# 4. Power List Map

def power_list(sample,index):
    res = list(map(pow,sample,index))
    return res

print(power_list([1,2,3,4],[0,1,2,3]))