list=[]
size=int(input("Enter size: "))
for i in range(size):
    num=int(input("Enter numbers: "))
    list.append(num)
print(list)
sum_even=0
sum_odd=0
for i in list:
    if i % 2 == 0:
        sum_even+=i
    elif i % 2 == 1:
        sum_odd+=i
print(sum_even-sum_odd)