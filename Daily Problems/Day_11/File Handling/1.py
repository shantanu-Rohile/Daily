# 1. Read Entire File

def read_file(name):
    try:
        with open (name,"r") as file:
            data= file.read()
    except Exception as e:
        return e
    else:
        return data    

print(read_file("demo.txt"))
    