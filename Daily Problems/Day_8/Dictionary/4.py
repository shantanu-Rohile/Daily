# 4. Remove Item(s) from a Given Set

def remove_item(sample,ele):
    for i in ele:
        for j in sample:
            if i==j:
                sample.discard(i)
                break
    return sample

sample = {1,2,3,4}

ele=[1,2]

print(remove_item(sample,ele))