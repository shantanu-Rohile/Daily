# 15. Random Line Reader

import random

def random_line_reader(name):
    with open(name,"r") as file:
        data = file.readlines()

    rand_line = random.randint(0,len(data)-1)

    return data[rand_line]


print(random_line_reader("new.txt"))