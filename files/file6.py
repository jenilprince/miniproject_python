data=""
with open ('original.txt','r') as file:
    r=file.read()
    data=data+r
print(data)
with open ('copy.txt','w') as file2:
    write=file2.write(data)
