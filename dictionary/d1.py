details={
    'Name': "David",
    'Age': 23,
    'City': "Kottayam"
}
print(details["Name"])
print(details['Age'])
details['Name']="Bob"
details['Gender']="M"
del details['Gender']
print(details)
if "Bob" in details['Name']:
    print("Yes")
else:
    print("No")
for key,value in details.items():
    print(key,value)