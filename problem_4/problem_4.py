def ispalidrome(num):
    list_num = list(map(int, str(num)))
    reverse_list_num = list_num[::-1]
    if(list_num == reverse_list_num):
        return True
    else:
        return False
res = 0
for i in range(100,1000):
    for j in range(100,1000):
        num = i*j
        if(ispalidrome(num)==True):
            if(res<num):
                res = num
print(res)
