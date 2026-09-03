# 33. Generate All Sublists
from itertools import combinations

def all_combinations(sample):
    combinations_list = []
    for i in range(0,len(sample)+1):
        combination = [list(x) for x in combinations(sample,i)]

        if len(combination)>0:
            combinations_list.extend(combination)

    return combinations_list

sample =(1,2,3)

print(all_combinations(sample))
