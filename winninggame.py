#BSCIt-05-0080/2024
#Mokeira Maiso
#Number guessing game
#generates random number beetween 1 and 10

import random

print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 10.")
print("Try to guess it!\n")

winning_number = random.randint(1, 10)
guess = None

while guess != winning_number:
    guess = int(input("Enter your guess: "))

    if guess < winning_number:
        print("too low, try again\n")
    elif guess > winning_number:
        print("too high, try again\n")
    else:
        print(" YOU WIN !!!! Well done!")
