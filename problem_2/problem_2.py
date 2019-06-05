x = 1
y = 1
sum1 = 0
result = 0

while(sum1 < 4000000):
   sum1 = (x+y)         
   if(sum1%2 == 0):
       result = result + sum1
   x = y
   y = sum1

print(result)
