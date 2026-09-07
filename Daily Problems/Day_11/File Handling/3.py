# 3. Append Text and Display

def append(name):
    with open(name,"a") as file:
        file.write("Graduated in 2026")


append("demo.txt")