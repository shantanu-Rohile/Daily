# 14. Sort Dictionary by Key

def sort_dic_by_key(sample):
    res = dict(sorted(sample.items(), key=lambda x: x[0]))
    return res

sample = {'c': 3, 'a': 1, 'd': 4, 'b': 2}

print(sort_dic_by_key(sample))