# 1. Sum Items in List

def sum (num_list):
    sum = 0

    for i in num_list:
        sum += i

    return sum

new_list = [1,2,3,4,5,6]

print(sum(new_list))
