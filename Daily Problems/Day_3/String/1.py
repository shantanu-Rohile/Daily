# 11. Remove odd index chars from a string.

def remove_char_with_odd_index(str):
    res = ""
    for i in range(len(str)):
        if i%2 ==0 :
            res += str[i]
    return res

print(remove_char_with_odd_index("Python"))
