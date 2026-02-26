#simple interest to prompt the user to enter principle,rate and time

principle=float(input("Enter the principle: "))
rate=int(input("Enter the rate: "))
time=int(input("Enter the time: "))

def simple_interest(principle,rate,time):
    simple_interest=principle*rate/100*time
    return simple_interest

print("The simple interest is: " ,simple_interest(principle,rate,time))

