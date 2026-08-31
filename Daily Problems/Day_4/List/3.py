def diff_lists(list1,list2):
    list1 = set(list1)
    list2 = set(list2)

    return list(list1-list2)


print(diff_lists([1,2,3,4,5,6,7,8],[4,5,6,7,8,9,10,11]))
