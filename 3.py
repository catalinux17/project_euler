from math import sqrt

n = 600851475143

for i in range(2, int(sqrt(n))):
    if n % i == 0:
        n /= i
        print(i)

