# 30. Count Frequency of List Elements

def freq(sample):
    frequency = {}

    for i in sample:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1
    return frequency

sample = [1,1,1,2,3,4,5,3,4,6,7,8,9,7,8,9,10,11]

print(freq(sample))

 