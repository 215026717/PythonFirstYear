def isprime(x):
    m = 2     
    while (m != x) or x == 2:
        if x / 2 < m and x != 1:
            return 1
        elif x % m == 0:
            return 0
        m += 1
        return 0
    return 0
x = int(input())
print(isprime(x))