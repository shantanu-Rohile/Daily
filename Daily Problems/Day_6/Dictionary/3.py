# 8. Merge Two Python Dictionaries

def merge_dic(d1,d2):
    d1.update(d2)
    return d1

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

print(merge_dic(d1,d2))