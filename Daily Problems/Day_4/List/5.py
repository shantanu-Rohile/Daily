# 21. Convert List to String

def convert_list_to_string(sample):
    res = ""
    for i in sample:
        res += i + " " 

    return res

list = ["papa pigs","apple","orange","watermelon"]


print(convert_list_to_string(list))