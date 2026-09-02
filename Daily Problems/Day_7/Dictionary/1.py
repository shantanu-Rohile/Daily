# 11. Multiply All Items in a Dictionary

def multiply_dict_items(sample):
    for key in sample:
        sample[key] = sample[key] * 2
    return sample

sample = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(multiply_dict_items(sample))