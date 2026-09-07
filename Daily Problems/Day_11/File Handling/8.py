# 8. Longest Words Finder

def longest_word(name):
    with open(name,"r") as file:
        data =file.read()

    list1= data.split()

    max = -1

    max_word = ""

    for i in list1:
        if len(i)>max:
            max = len(i)
            max_word = i

    print(max_word)

longest_word("demo.txt")
