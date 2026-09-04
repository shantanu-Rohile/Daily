# 16. Convert a Tuple to a Dictionary

# def tuple_dic(sample):
#     res = dict.fromkeys(sample)
#     return res

# sample = (1,2,3,4,5)

# print(tuple_dic(sample))


def tuple_dic(sample):
    res = dict(sample)
    return res

sample = ((1,2),(3,4))

print(tuple_dic(sample))