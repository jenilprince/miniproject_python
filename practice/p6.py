num=int(input("Enter a number: "))
string=str(num)
sum_even=0
for i in string:
    if int(i)%2==0:
        sum_even+=int(i)
print(sum_even)