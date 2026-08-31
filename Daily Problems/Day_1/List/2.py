# 2. Multiply Items in List

def mul (num_list):
    res = 1
    for i in num_list:
        res *= i
    return res

number_list = [1,2,3,4,5,6]

print(mul(number_list))

