# 8. Convert Numbers to Strings Map

def conversion(sample):
    res = list(map(lambda x : str(x),sample))
    return res

print(conversion([1,2,3,4,5]))