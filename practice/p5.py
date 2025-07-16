list=[]
rev=[]
size=int(input("Enter size: "))
for i in range(size):
    num=int(input("Enter number: "))
    list.append(num)
for i in range(size):
    rev.append(list[size-i-1])
print(rev)
