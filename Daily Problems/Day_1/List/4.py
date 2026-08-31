# 4. Get Smallest Number in List

def samll(num_list):
    smallest_num = 1000000
    for i in num_list:
        if i <= smallest_num :
            smallest_num = i
    return smallest_num

num_list = [42, 12, 89, 3, 54, 71, 23, 95, 11, 60]

print(samll(num_list))