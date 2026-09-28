# 3. Handle FileNotFoundError Exception When Opening a File

def error(f):
    with open (f,'r') as file:
        res = file.read()
        return res

try:
    error("new.txt")
except Exception as e:
    print(e)
