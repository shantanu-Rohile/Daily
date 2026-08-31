# 22. Sort string lexicographically.

def sort_lexilogicaly(sample):
    list1=[]
    for i in sample:
        list1.append(i)
    list1.sort()

    return "".join(list1)


print(sort_lexilogicaly("JVM"))