# 32. Check if List Contains Sublist

def is_sublist(sample1,sample2):
    for i in range(len(sample2)):
        if sample2[i] not in sample1:
            return False
    return True

sample1=[1,2,3,4,5,6,7]

sample2 = [2,3,9]

print(is_sublist(sample1,sample2))
        
