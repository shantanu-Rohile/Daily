# 7. Dictionary with Keys 1 to 15 and Their Squares

def dictionary_with_squares():
    d={}
    for i in range(1,16):
        d.update({i:i**2})
    return d

print(dictionary_with_squares())