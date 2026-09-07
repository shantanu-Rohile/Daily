# 5. File to List

def read_last_n_lines(name):
    with open(name, "r") as file:
        data = file.readlines()
    return data

print(read_last_n_lines("demo.txt"))