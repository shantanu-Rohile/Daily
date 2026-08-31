# 21. Uppercase string if 2+ uppercase chars in first 4.

def type_conversion(str):
    count = 0
    for i in range(len(str)):
        if i<4 and (ord(str[i]) >64 and ord(str[i])<91)  :
            count =count+1
    if count > 2 :
        return str.upper()

    return str

print(type_conversion("PYThon"))