# 2. Read First N Lines

from itertools import islice

def read_n_lines(name,n):
    with open(name,"r") as file:
        for line in islice(file,n):
            print(line)


read_n_lines("demo.txt",2)