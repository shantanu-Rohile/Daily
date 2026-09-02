# 6. Generate Dictionary of Numbers and Their Squares

def dictionary_with_squares(num):
    dci={}
    for i in range(num):
        dci.update({i:i**2})
    return dci

print(dictionary_with_squares(5))