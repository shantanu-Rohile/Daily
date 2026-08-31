# 10. Swap first and last chars of a string.

def swap (str):
    if len(str) > 1 :
        first = str[0]
        last = str[-1]
        middle = str[1:-1]

        return  last + middle + first
    return str


print(swap("tac"))