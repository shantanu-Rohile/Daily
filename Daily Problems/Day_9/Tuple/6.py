# 21. Replace the Last Value of Tuples in a List

def change_last_value(sample,value):
    for i in range(len(sample)):
        if type(sample[i]) == type(()):
            sample[i]=list(sample[i])
    for i in range(len(sample)):
        if type(sample[i]) == type([]):
            sample[i][len(sample)-1] = value
    for i in range(len(sample)):
        if type(sample[i]) == type([]):
            sample[i]=tuple(sample[i])  
    return sample    


l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

print(change_last_value(l,100))