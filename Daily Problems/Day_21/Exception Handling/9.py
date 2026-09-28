# 9. Handle UnicodeDecodeError When Opening a File

def ude(f):
    try:
        with open(f,'r',encoding='utf-8') as file:
            res= file.read()
            print(res)
    except UnicodeDecodeError:
        print("change ecoding and try again")

ude("new.txt")