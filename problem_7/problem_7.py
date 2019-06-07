def nth_prime(n):
    count = 2
    for i in range(3, n**2, 2):
        a = 1
        while a*a < i:
            a += 2
            if i % a == 0:
               break
        else:
            count += 1
        if count == n:
            return i
print("enter position")
n = int(input())
print(nth_prime(n))
