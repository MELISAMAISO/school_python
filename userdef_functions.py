#python functions
def myName():
    print("My name is Melissa")

#function call
myName()

#to add parameters to a function

def sum(a,b):
    sum=a+b
    return sum

#function call
print(sum(10,20))#use print function to see the function on the screen

def sum(c,d):
    sum=c+d
    return sum

e=sum(20,20)#calling a function using the variable e
print(e)

#prompting the user to enter the pet name and age
name=input("Enter the pets name ")
age=int(input("Enter the pets age "))
def myPet(name,age):
    print("My pet name is "+name+" and it is "+str(age)+" years old")#we place the age to a str that is type casting because age is an integer and we want to concanate it with another string which is name
    print(f"My pet name is {name} and it is {age} years old")#we place the f because we are using the curlbraces 

myPet(name,age)
