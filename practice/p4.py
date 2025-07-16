#STRONG NUMBER
num=145
#find factorial of digits

sum_fact=0
temp=num
while temp>0:
    last=temp%10
    fact=1
    for i in range(1,last+1):
        fact*=i
    sum_fact+=fact
    temp//=10
print(sum_fact)


