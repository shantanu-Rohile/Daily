# 24. Append One List to Another

def append_list(sample1,sample2):
    sample1.extend(sample2)
    return sample1


fruits = ["apple", "banana", "cherry"]

numbers = [10, 20, 30, 40, 50]

print(append_list(fruits,numbers))