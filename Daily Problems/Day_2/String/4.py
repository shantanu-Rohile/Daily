# 9. Remove nth character from a string.

def remove_nth (str,index):
    first = str[:index]
    second = str[index + 1:]
    result = first + second

    return result

print(remove_nth("diffeerence",4))