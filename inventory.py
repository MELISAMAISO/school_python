#BSCIT-05-0080/2024
#MELISA MAISO

inventory={}

n=int(input("How many items do you want to add?"))

for r in range(n):
    name=input("Enter item name: ")
    quantity=int(input("Enter quantity:"))
    
    inventory[name]=inventory.get(name,0)+quantity

want_search=input("Do you want to search an item?(yes/no):")

search=want_search=="yes"
if search:
    item=input("Enter item name to search : ")
    print(item,inventory.get(item,"item not found"))

total=0
for i in inventory.values():
    total +=i

print("Total quantity: ",total)
