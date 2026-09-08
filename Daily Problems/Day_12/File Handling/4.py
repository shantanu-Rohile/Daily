# 14. Combine Lines from Two Files

def combine_lines(file1,file2):
    with open(file1,"r") as file:

        data = file.readlines()

        line1 = data[0]

        line1_final = line1[0:len(line1)-1]

    with open(file2,"r") as file:

        data = file.readlines()

        line2 = data[0]

        line2_final = line2[0:len(line2)-1]

    return line1_final + " "+ line2_final

print(combine_lines("new.txt","demo.txt"))

