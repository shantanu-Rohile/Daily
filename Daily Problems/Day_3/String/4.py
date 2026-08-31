# 14. Sort distinct words in comma-separated input.

def sort_words(sample):
    for i in range(len(sample)):
        for j in range (len(sample)-i-1):
            if sample[j][0] > sample[j+1][0] :
                temp = sample[j]
                sample[j] = sample[j+1]
                sample[j+1] = temp
            elif sample[j][0] == sample[j+1][0] :
                small = ""
                if len(sample[j]) >= len(sample[j+1]):
                    small = sample[j+1]
                else:
                    small = sample[j]
                for k in range(len(small)):
                    if sample[j][k] > sample[j+1][k] :
                        temp = sample[j]
                        sample[j] = sample[j+1]
                        sample[j+1] = temp
                        break
                   
    return sample


words = ["cat", "car", "bat", "dog", "cot", "bar"]

print(sort_words(words))




