# 2. Count character frequency in a string.

str= "shantanurohile@gmail.com"
frequency = {}
for i in str:
    if frequency.get(i):
        frequency[i] = frequency.get(i) + 1
    else :
        frequency.update({i:1})


print(frequency)
