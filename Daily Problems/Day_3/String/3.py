# 13. Display input in upper and lower case.

def convert_lower(str):
    res=""
    for i in range(len(str)):
        if ord(str[i]) > 64 and ord(str[i]) < 90 :
                ascii = ord(str[i])
                res += chr(ascii + 32)
        else:
            res += str[i]

        

    return res


print(convert_lower("Hi, My name's Shantanu."))