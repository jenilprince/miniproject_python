with open('greeting.txt','w') as file:
    file.write("Welcome to Python File Handling!")
with open('greeting.txt','r') as file1:
    print(file1.read())