# 25. Select Random Item from List

import random
def select_random_item(sample):
    num = random.randint(0,len(sample)-1)
    return sample[num]

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

print(select_random_item(fruits))