# 6. Handle IndexError in List Operations

def i_e(lst):
    try:
        print(lst[10000])
    except IndexError:
        print("Index out of range")

i_e([1,10,20,30,40])