# 16. Insert string into middle of another.
def insert(str1,str2):
    list1 = str1.split()
    res = ""
    if(len(list1)==1):
        length=len(str1)
        for i in range(length):
            if i == length/2 :
                res += " "+str2+" "
            res += str1[i]
    else:
         length=int(len(list1)/2)
         list1.insert(length,str2)
         res = " ".join(list1)



    return res

print(insert("Python 3.0", "HTML"))
            

