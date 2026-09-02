# 30. Print numbers with 2 decimal places.

def numbers_with_2decimal(str):
    res = ""
    for i in range(len(str)):
        if str[i] == ".":
            if i+1 <=len(str)-1:
                res += str[i]+ str[i+1]
                if i+2 <len(str)-2:
                    res += str[i+2]
                else :
                    res += "0"
            else:
                res +=str[i]+ "00"
            break
        res += str[i] 
    return res

print(numbers_with_2decimal("12.6"))