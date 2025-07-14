key=["Name","Age","Gender","City"]
value=["Bob","A","Male","Kottayam"]
details=dict(zip(key,value))
print(details)
c=sorted(details.items(),key=lambda x:x[1])
print(c)