from math import sqrt

def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True



counter = 0

for i in range(2, 100_000_000):
    if is_prime(i):
        counter += 1

    if counter == 6:
        print(i)

    if counter == 10_001:
        print(i)
        exit()
