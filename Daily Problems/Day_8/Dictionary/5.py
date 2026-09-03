# 5. Remove an Item from a Set if Present

def remove_item_if_present(sample,ele):
    sample.remove(ele)
    return sample

sample={1,2,3,5,6,4}

ele = 7

print(remove_item_if_present(sample,5))