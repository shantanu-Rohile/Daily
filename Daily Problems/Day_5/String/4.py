# 24. Check if string starts with specified chars.

def if_exeist(sample,charracter):
    if sample[0:len(charracter)]==charracter:
        return True
    else:
        return False

print(if_exeist("Nano Technology",'Nano'))