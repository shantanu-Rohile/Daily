# 4. Replace first char occurrences with $.

str = "restart"

first = str[0]
list_str = []
for i in range(len(str)):
    list_str.append(str[i])


for i in range(len(list_str)):
    if list_str[i] == first and i!=0:
        list_str[i] = "$"


res = "".join(list_str)

print(res)

