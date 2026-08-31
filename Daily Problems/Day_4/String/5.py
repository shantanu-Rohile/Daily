# 20. Reverse string if length is a multiple of 4.

def reverse_String(str):
    if len(str)%4 ==0 :
        res =str[::-1]
        return res
    return str

print(reverse_String("Shantanu"))
