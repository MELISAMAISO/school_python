#MOKEIRA MAISO
#Inheritance is when a child class gets properties and methods from another class(parent class)
#reuse code, avoid repetition, organize programs better

#Single Inheritance, one child inherits from one parent

class Animal:
    def speak(self):#self is needed as the first parameter
        print("Animal makes sound")

class Dog(Animal):
    pass

dog1=Dog()#creating the object dog1
dog1.speak()#calling the object

#Multiple Inheritance one child inherits from more than one parent
class Mother:
    def skill1(self):
        print("cooking")

class Father:
    def skill2(self):
        print("driving")

class Child(Mother, Father):
    pass

child1=Child()
child1.skill1()
child1.skill2()

#Multilevel inheritance
#A class inherit from a class that already inheritedfrrom anoter class

class Animal:
    def eat(self):
        print("Animal eating")

class Dog(Animal):
    def bark(self):
        print("Dog barking")

class Puppy(Dog):
    def play(self):
        print("Puppy playing")

P=Puppy()
P.eat()
P.bark()
P.play()         


#Hierarchical inheritance
#Multiple child classes inherit from the same parent class.

class Animal:
    def eat(self):
        print("Animal eating")

class Dog(Animal):
    def bark(self):
        print("Dog barking")

class Cat(Animal):
    def meow(self):
        print("Cat meowing")

d=Dog()
c=Cat()

d.eat()
d.bark()

c.eat()
c.meow()

#Hybrid inheeritance
#Acombination of two or more types of inheritance

class A:
    def methodA(self):
        print("Class A")

class B(A):
    def methodB(self):
        print("Class B")

class C(A):
    def methodC(self):
        print("Class C")

class D(B,C):
    def methodD(self):
        print("Class D")

obj=D()
obj.methodA()
obj.methodB()
obj.methodC()
obj.methodD()        


