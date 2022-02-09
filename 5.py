from functools import reduce
import math

def evenly_divisible(n: int) -> bool:
    for i in range(22, 42, 2):
        if not n / i:
            return False

    print(n)

    return True


number = 20
primes = []


for n in range(1, number + 1):
    for i in range(2, 21):
        if n % i == 0:
            n /= i
            primes.append(i)


primes = list(set(primes))

lcm = reduce(lambda x, y: lcm(x, y)z, primes)


print(primes)
print(lcm)


