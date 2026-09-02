def sum(d):
    sum = 0
    for key,value in d.items():
        sum += value
    return sum

d = {'a': 100, 'b': 200, 'c':300}
print(sum(d))
