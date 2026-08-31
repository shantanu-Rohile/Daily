# 7 remove Duplicates from List

# Method one

# set(_ample)

def remove_duplicates(sample):
    frequency = {}
    for i in sample:
        if i in frequency:
            for key,value in frequency.items():
                if key == i :
                    frequency[i] = frequency.get(key) + 1
        else:
            frequency.update({i:1})

    for key,value in frequency.items():
        if frequency.get(key) == 2 :
            sample.remove(key)
            frequency[key] = frequency.get(key)-1

    print(sample)
                


sample = [1, 2, 2, 3, 4, 4, 5]


remove_duplicates(sample)