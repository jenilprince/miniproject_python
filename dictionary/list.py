def even(list):
    new=[]
    for i in list:
        if i%2==0:
            new.append(i)
    print(f"Even list: {new}")
even([1,23,34,2,64,32,11,345,98,54,10,43,5,6])