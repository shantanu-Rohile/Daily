# 5. Remove an Item from a Set if Present

s1= {1,2,3,4,5,6,7,8}

try:
    s1.discard(11)

    print(s1)

except Exception as e:

    print(e)
