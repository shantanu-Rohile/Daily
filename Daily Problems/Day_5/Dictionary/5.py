# 5. Iterate Over Dictionary Using For Loops
def iterate(sample):
    for i in sample.items():
        print(i)


prices = {
    "apple": 1.50,
    "banana": 0.75,
    "orange": 1.20
}


iterate(prices)