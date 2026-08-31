# 7.sorting a group of strings

def sort():
    sample = []
    num = int(input("Number of strings to sort : "))
    for i in range(num):
        word = input("Type String here : ")
        sample.append(word)

    for i in range(len(sample)):
        for j in range(len(sample)-i-1) :
            if sample[j][0] > sample[j+1][0]:
                temp = sample[j]
                sample[j]=sample[j+1]
                sample[j+1]=temp
            elif sample[j][0] == sample[j+1][0]:
                small = ""
                if len(sample[j]) < len(sample[j+1]):
                    small = sample[j]
                else:
                    small = sample[j+1]
                for k in range(1,len(small)-1):
                    if sample[j][k] != sample[j+1][k] :
                        if sample[j][k] > sample[j+1][k]:
                            temp = sample[j]
                            sample[j]=sample[j+1]
                            sample[j+1]=temp
                        break
    return sample


print(sort())