# 10. Find Words Longer Than n

def greatre_n(str,n):
    word = ""
    count = 0
    for i in range(0,len(str)):
       
        if str[i] == " " or str[i] == "." or str[i] =="!" or str[i] =="?" or i == len(str)-1  :
            if len(word) > n :
                count += 1
            word = ""
        else :           
            word += str[i]

    return count

str = "Write a Python program to find the list of words that are longer than n from a given list of words."
print(greatre_n(str,4))