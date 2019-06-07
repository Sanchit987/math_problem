sum_of_square = 0
square_of_sum = 0
su = 0
for i in range(1,101):
    sum_of_square += i*i
    su += i
square_of_sum = su*su
res = square_of_sum - sum_of_square
print(res)
