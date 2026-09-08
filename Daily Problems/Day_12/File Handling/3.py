# 13. Copy File Contents

def copy_contents(orignal,copy):
    with open(orignal,"r") as file:
        data = file.readlines()

    with open(copy,"w") as file:
        file.writelines(data)


copy_contents("new.txt","copy.txt")