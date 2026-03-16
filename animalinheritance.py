#BSCIT-05-0080/2024
#MOKEIRA MAISO

class Animal:
    def fur(self):
        print("I have furall over my body")

class Dog(Animal):
    def bark(self):
        print("Dog barking")

class Puppy(Dog):
    def play(self):
        print("I pay all the time")

#creating an object
bosco=Puppy()

bosco.play()
bosco.bark()
bosco.fur()


