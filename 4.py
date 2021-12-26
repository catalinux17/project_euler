
def palindrome(n: int) -> bool:
    str_n = str(n)
    size = len(str_n)
    for i in range(size//2):
        if str_n[i] != str_n[-1 - i]:
            return False

    return True

palindromes = []

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if palindrome(i*j):
            palindromes.append(i*j)

palindromes.sort()
print(palindromes[-1])
    
