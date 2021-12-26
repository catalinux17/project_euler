

def fibonacci(n: int):
    if n < 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

numbers = []
i = 1

while True:
    fib_number = fibonacci(i)
    if fib_number < 4_000_000:
        numbers.append(fib_number)
    else:
        break
    i += 1

numbers = sum( filter(lambda x : x % 2 == 0, numbers) )
print(numbers)
