# 17. Check If All Numbers Are Prime

def is_prime(num):
    if num ==1 :
        return "1 is nither prime nor composite"
    for i in range(2,num):
        if num%i==0:
            return "not prime"

    return "prime"

print(is_prime(21))