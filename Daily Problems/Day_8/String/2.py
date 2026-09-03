# 32. Print numbers without decimal places.

def without_decimal(num):
    num = f"{num:.0f}"
    return num

print(without_decimal(-12.99))