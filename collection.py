#lists
items=[10,True,"Bob",2.3]

#Tuple
items=(1,3.2,5,5)

#set
items={"Bob",10,20,30}

#creating a list

students=["John","Jane","James"]
print(students)

#the list()constructor
students=list((["John","James","Jane"]))
print(students)

#accesssing individual items from the list
items=["Bob",10,True,3.142]
print(items)
print(items[0])
print(items[3])
print (items[-1])

#to change element at an index
fruits=["apple","banana","cherry","orange"]
fruits[1]="blackcurrant"
print(fruits)#changes banana to blackcurrant when printed

#inserts the fruit function when printed at index 2
fruits.insert(2,"passion")
print(fruits)

fruits[1:3]=["watermelon","fanta"]
print(fruits)

#adds an item at the end of the list
fruits.append("mangoes")
print(fruits)

#removes an item from the list
fruits.remove("cherry")
print(fruits)

fruits.reverse()

#extend is used to combine two lists that is name and cars
names=["peter","john","Ethan"]
cars = ["toyota", "BMW","Audi","Benz"]

names.extend(cars)
print(names)

#
for i in range(len(fruits)):
    print(fruits[i])
    