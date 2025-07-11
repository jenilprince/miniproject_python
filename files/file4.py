with open("Notes.txt", "r") as file:
    count=0
    for i in file.read():
        if i == "\n":
            count+=1
    print("Count: ",count)



