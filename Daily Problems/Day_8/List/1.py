# 31. Count Elements in List Within Range

def count(sample,range):
    count =0
    for i in sample:
        if i>= range[0] and i<=range[1]:
            count = count+1
    return count

sample = [10, 20, 30, 40, 40, 40, 70, 80, 99]

range=(10,40)

print(count(sample,range))

