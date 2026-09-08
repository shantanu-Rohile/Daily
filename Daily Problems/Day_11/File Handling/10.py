# 10. Word Frequency Counter

def word_frequency(name):
    with open(name,"r") as file:
        data= file.read()

        list1= data.split()
    frequecy = {}

    for i in list1:
        if i in frequecy:
            frequecy.update({i:frequecy.get(i)+1})
        else:
            frequecy.update({i:1})
    return frequecy

print(word_frequency("demo.txt"))

