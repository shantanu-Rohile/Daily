# 12. Remove Specific Elements from List

def remove_element(element,sample):
    res = []
    for i in sample:
        if i == element :
            continue
        else :
            res.append(i)
    return res

sample = ["apple", "banana", "cherry", "banana"]

print(remove_element("banana",sample))