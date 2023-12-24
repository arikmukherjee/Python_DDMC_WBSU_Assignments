# Check the number prime or not

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
num = 17
if is_prime(num):
    print(num ,"is a prime number.")
else:
    print(num ,"is not a prime number.")