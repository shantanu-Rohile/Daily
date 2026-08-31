# 17. Repeat last 2 chars of a string 4 times.

def repeat_last_two(str):
    last = str[-2:]
    for i in range(4):
        print(last,end=" ")

repeat_last_two("Python")