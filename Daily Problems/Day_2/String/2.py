# 7. Replace 'not'...'poor' with 'good'.



def replace(str):
    list = str.split()

    size = len(list)

    res_list = list.copy()

    for i in range(size) :
        if list[i] == "not":
            print("yes")
            res_list.pop(i)
        elif "poor" in list[i] :
            res_list[i-1] = "good"

    res = " ".join(res_list)

    print(res)

str = "The lyrics is not that poor!"

replace(str)