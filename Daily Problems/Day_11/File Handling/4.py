# 4. Read Last N Lines

def read_last_n_lines(name, n):
    with open(name, "r") as file:
        data = file.readlines()
        for line in data[-n:]:
            print(line, end="")

read_last_n_lines("demo.txt", 2)