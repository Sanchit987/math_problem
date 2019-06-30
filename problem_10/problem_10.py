def s(n):
    su = 0
    sieve =  [True] * n
    for x in range(2, n):
        if sieve[x]:
            su += x
            for i in range(x**2, n, x):
                sieve[i] = False
    return su

print(s(2000000))
