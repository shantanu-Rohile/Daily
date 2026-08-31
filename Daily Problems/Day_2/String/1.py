# 6. Add ing or ly to a string.


def add_ly_ing (str):
    if len(str) > 2 :
        last = str[-3:]
        if last == "ing" :
            res = str + "ly"
            return res
        else :
            res = str + "ing"
            return res
    return str


print(add_ly_ing("string"))