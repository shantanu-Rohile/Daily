# 6. Sort Tuples by Last Element

def sort_list(sample):
    for j in range(len(sample)):
        for i in range(0,len(sample)-j-1):
                element1 = sample[i][1]
                element2 = sample[i+1][1]

                if (element1 > element2):
                    temp = sample[i+1]
                    sample[i+1] = sample[i]
                    sample[i] = temp

                    
    return sample
        
            

sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(sort_list(sample))

