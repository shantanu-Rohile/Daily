# 3. Listify Strings Map

def listify_list(sample):
    res = list(map(lambda x : list(x),sample))
    return res

print(listify_list(["red","orange","green","blue"]))