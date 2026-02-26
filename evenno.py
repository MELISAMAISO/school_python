#create a function that takes a list
# of integers as input and returns a new list containing only the even number

def evennumbers(numbers):#function to check if the number is even
    even_numbers=[]
    for number in numbers:
        if number %2==0:#if the number is divided by 2 and returns zero it is even 
            even_numbers.append(number)

    return even_numbers   

my_input=input("Enter numbers with spaces in btwn: ")#prompt the user to input numbers

numberlist=my_input.split()#the numbers in my input to be broken into a list using .split()
numberlist=[int(num)for num in numberlist]#the numbers in numberlist to be converted to integer

result=evennumbers(numberlist)

print("Even numbers are: ",result)



#Create a function that take a list checks if the list contains only odd number
oddnumber=input("Enter your numbers: ")

def odddigits(digits):
    odd_digits=[]
    for digit in digits:
        if digit %2!=1:
            odd_digits.append(digit)

oddlist=oddnumber.split()
oddlist=[int(dig)for dig in oddlist]
answer=odddigits(oddlist)

print("Odd numbers are:",answer)

