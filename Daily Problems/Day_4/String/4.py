# 19. Get substring before a specific character.

def substring(str):
    res = 0
    result=""

    for i in range(len(str)-1,0,-1):
        if str[i]== "." or str[i]== "/" or str[i]== "\\" or str[i]== ":"  :
            break
        else :
            res+=1

    for i in range(0,len(str)-res):
            result += str[i]
    return result



print(substring("https://www.w3resource.com/python"))