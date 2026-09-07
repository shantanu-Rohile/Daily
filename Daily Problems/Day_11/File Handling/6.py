# 6. File to Variable

from itertools import islice

def variable_read(name):
    res = []
    with open(name,"r") as file:
        data = file.readlines()
        length = len(data)

    for i in range(length):
        value = data[i]
        print(value)
        
variable_read("demo.txt")