# 20. Access List Indices

def index(list,index):
    count = 0
    for i in list:
        if count == index:
            return i
        count = count +  1
    return -1


list = ["papa pigs","apple","orange","watermelon"]

print(index(list,2))