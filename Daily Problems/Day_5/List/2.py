# 23. Flatten Shallow List

# flattening list : making multiple demensional list into 1d

# we can also use in-built .faltten() function

def flatten_list(sample):
    res = [] 
    for i in range(len(sample)):
        for j in range(len(sample[i])):
            res.append(sample[i][j])
    return res

sample =  [
    [1, 2, 3],  
    [4, 5, 6],  
    [7, 8, 9]   
]

print(flatten_list(sample))