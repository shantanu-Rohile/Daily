# 4. Check Key Existence in Dictionary

def exeist(sample, key):
    if key in sample:
        print(key," exeist in dictionary")
    else:
        print(key," does not exeist in dictionary")


sample = {"name":47, "age" :22, "id": 23, "phone number" : 9011223344}

exeist(sample,"name")