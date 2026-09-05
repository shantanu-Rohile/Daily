# 11. Sum Elements Map
from array import array 
def sum_elements(sample):
    sum = 0
    sample=map(int,sample)
    for i in sample:
        sum += i
    return sum

sample = array('u',['1','2','3','4','5','6','6','7'])

print(sum_elements(sample))