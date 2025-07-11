name=input("Enter your name: ")
age=input("Enter your age: ")
with open('user_info.txt','w') as file:
    file.write(name)
    file.write(age)
with open('user_info.txt','r') as file1:
    print(file1.read())