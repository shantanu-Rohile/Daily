# 2. Validate Integer Input and Raise ValueError

def add(x,y):
    return x+y

try:
    add(10,'20')
except Exception as e:
    print(e)