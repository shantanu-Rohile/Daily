# 9. Line Count
def line_count(name):
    
    with open(name,"r") as file:
        data = file.readlines()
        length = len(data)
        count = 0
    for i in range(length):
        count +=1
    print(count)


line_count("demo.txt")
