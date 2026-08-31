# 14. Remove Even Numbers from List

def remove_even_element(sample):
    res = []
    for i in sample:
        if i % 2 ==0 :
            continue
        else :
            res.append(i)
    return res

sample = [1,2,4,5,6,7,867,64564,132124,3431]

print(remove_even_element(sample))