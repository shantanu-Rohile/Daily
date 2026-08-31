# 3. Get string of first and last 2 chars.

str= "w"

count = 0
for i in str:
    count = count +1


length = count



res =""

first_cha = ""

last_cha = ""

if length > 1 :
    first_cha = str[0]+str[1]
if length > 3 :
    last_cha = str[length-2]+str[length-1]

res = '"' + first_cha + last_cha +'"'

print(res)