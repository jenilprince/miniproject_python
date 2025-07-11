## To display numbers btw 100 and 200 where sum of digits is even
for i in range(100,201):
    sum_dig=0
    for j in str(i):
        sum_dig+=int(j)
    if sum_dig%2==0:
        print(i)



