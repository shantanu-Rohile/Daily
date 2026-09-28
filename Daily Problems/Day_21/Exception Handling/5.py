# 5. Handle PermissionError Exception When Opening a File

def per(f):
    try:
        with open(f,'r') as file:
         res = file.read()
        print(res)
    except PermissionError:
        print("Permission denied")


file_name = input("file name : ")

per(file_name)

    