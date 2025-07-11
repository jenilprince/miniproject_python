with open('data.txt','r') as file:
    word="Python"
    if word in file.read():
        print("Found")
    else:
        print("Not Found")
