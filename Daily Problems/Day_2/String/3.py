# 8. Find longest word in a list.

def longest(sample):
    length=0
    max_length=""
    for i in sample:
        if len(i) > length : 
            max_length = i
            length = len(max_length)
    return max_length

sample = ["apple", "banana", "strawberry", "kiwi"]

print(longest(sample))