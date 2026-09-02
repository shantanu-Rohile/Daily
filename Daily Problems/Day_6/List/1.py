

def if_identical(list1,list2):
    first=list1[0]
    second=list1[1]
    index2=-1
    if len(list1)==len(list2):
        for i in range(len(list2)):
            if list2[i]==first:
               if list2[(i + 1) % len(list2)] == second:
                    index2 = i
                    break
    if index2==-1:
        return False
    if len(list1)==2:
        return True
    for i in range(2,len(list1)):
        if list1[i] != list2[(index2 + i) % len(list2)]:
            return False
    return True


list1=[1,2,3,4]
list2=[4,1,2,3,]

print(if_identical(list1,list2))