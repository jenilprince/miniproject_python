list1=[]
list2=[]
size=int(input("Enter size: "))
for i in range(size):
    int(input("Enter number for list1: "))
    list1.append(i)
for i in range(size):
    int(input("Enter number for list2: "))
    list2.append(i)
set1=set(list1)
set2=set(list2)
print(set1==set2)