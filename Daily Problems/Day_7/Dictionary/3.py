# 13. Map Two Lists into a Dictionary

def map_dic(sample1,sample2):
    return dict(zip(sample1,sample2))

sample1 = ['a', 'b', 'c', 'd']
sample2 = [1, 2, 3, 4]

print(map_dic(sample1,sample2))