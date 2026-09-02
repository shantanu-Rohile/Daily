# 27. Remove indentation from text.

def remove_indentation(sample):
    res= sample.lstrip()
    return res

sample ="    Hi, How are you"

print(remove_indentation(sample))