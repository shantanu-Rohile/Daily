# 11. Check Common Member Between Two Lists

def common_elements(sample1,sample2):
    common_elements =[]
    for i in sample1:
        for j in sample2:
            if i == j :
                common_elements.append(i)
    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(common_elements(list1,list2))