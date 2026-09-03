#  31. Print numbers with sign (2 decimals).

def num_with_sign(num):
    new_num = float(num)
    new_num = round(new_num,2)

    if new_num > 0 :
        res = str(new_num)

        res = "+" + res

        return res
    elif new_num == 0 :
        return "0"
    else :
        res = str(new_num)
        return res

    return 0

print(num_with_sign(-12.9999))