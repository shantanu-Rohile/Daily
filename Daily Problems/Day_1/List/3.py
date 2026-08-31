# 3. Get Largest Number in List


def large(num_list):
    largest_num = -1000
    for i in num_list:
        if i >= largest_num:
            largest_num = i

    return largest_num

num_list = [42, 12, 89, 3, 54, 71, 23, 95, 11, 60]

print(large(num_list))