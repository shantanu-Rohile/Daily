# 36. Get Variable ID or String

def get_var_id(str):
    return id(str)


var = "shantanu rohile"

print(get_var_id(var))