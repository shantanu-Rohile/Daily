# 7. File to Array
import numpy as np

def array_data(name):
    

    with open(name,"r") as file:
        data = file.readlines()
        length = len(data)
        
        arr = np.empty(length, dtype=object)
        
        for i in range(length):
            arr[i] = data[i]
    return arr

print(array_data("demo.txt"))
