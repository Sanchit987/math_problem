from math import gcd
ls  = []
for i in range(2,21):
    ls.append(i)

lcm = ls[0]
for i in ls[1:]:
  lcm = int(lcm*i/gcd(lcm, i))
print(lcm)
