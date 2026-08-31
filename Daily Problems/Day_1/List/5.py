# 5. Count Strings with Same Start and End

def count_string_same_letters (sample):
    count = 0
    for i in range(len(sample)):
        start = sample[i][0]
        end = sample[i][-1]
        if start == end and len(sample[i])>1 :
            count += 1
    return count

sample = ["abc", "aba", "xyz", "hello", "a", "level", "test", "radar", "1231"]


print(count_string_same_letters(sample))


