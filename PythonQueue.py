names=[]
for x in range(10):
    name=input("enter name: ")
    names.append(name)
print(names)
for x in range(len(names)):
    print(names.pop(0))
print(names)
