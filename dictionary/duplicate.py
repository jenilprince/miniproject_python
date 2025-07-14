a={'mark':[1,2,1],
   'age':[12,18,12]}
for key in a:
    a[key]=list(set(a[key]))
print(a)