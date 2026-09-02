# 12. Remove a Key from a Dictionary

def remove_key_from_dict(sample,k):
    if k in sample:
        sample.pop(k)
    return sample