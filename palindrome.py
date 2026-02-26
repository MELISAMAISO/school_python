#python function to check if a string is a palindrome
#A palindrome is a word that reads the same forward and backward example madam,racecar,level

def palindrome(word):#def creating a machine palindrome name of the machine word-what we put inside a machine 
    if word==word[::-1]:#[::-1]flip words backword
        return True
    else:
        return False

userinput=input("Enter a word to check if it is a palindrome: ")
if palindrome(userinput):
    print("Yes, your word is a palindrom!!")
else:
    print("No!, your word is not a palindrome")    