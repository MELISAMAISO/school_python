#BSCIT-05-0080/2024
#MOKEIRA MAISO

names=[]
n=int(input("How many names do you want to enter? "))

for i in range(n):
    name=input("Enter name :")
    names.append(name)

names=list(set(names))

names.sort()

print("sorted names with no duplicates: ")
print(names)
print("The total number of names",len(names))