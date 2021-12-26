from math import sqrt

def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

sum = 0

for i in range(2, 2_000_000):
    if is_prime(i):
        sum += i


print(sum)
