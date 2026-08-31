# 22. Find Index of List Item

def find_index(sample,element):
    for i in range(len(sample)) :
        if sample[i] == element :
            return i

    return -1

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(find_index(days_of_week,"Monday"))
