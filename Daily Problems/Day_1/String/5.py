#5. Swap first 2 chars of 2 strings.

str1= "car"

str2 = "bat"

first_str1 = str1[:2]
first_str2 = str2[:2]

last_str1 = str1[2:]
last_str2 = str2[2:]

res = [first_str1 + last_str2 , first_str2 + last_str1]

print(res)