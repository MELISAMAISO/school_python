#set items are unordered,unchangable and DO NOT allow duplicate values
#unchangable means you cannot change an item once a set is created but items can be add or removed to the set

myset={"cherry","mango","banana"}
print(myset)

#adding items to a set use add()
myset.add("orange")
print(myset)

#To get the length of a set
print(len(myset))

#a set can be of any datatype
set1 = {"abc", 34, True, 40, "male"}
print(set1)

#to add items from another set use update()
myset.update(set1)
print(myset)