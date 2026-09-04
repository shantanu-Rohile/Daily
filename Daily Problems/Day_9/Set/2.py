# 12. Remove All Elements from a Given Set

def clear_set(sample):
    copy_set=sample.copy()
    for i in copy_set:
        sample.remove(i)

    return sample

sample = {1,2,3}

print(clear_set(sample))