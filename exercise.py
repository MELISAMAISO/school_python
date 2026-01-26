#BSCIT-05-0080/2024
#MOKEIRA MAISO

hours=int(input("Enter hours:"))
rate_per_hour=float(input("Enter rate per hour:"))
print(hours,rate_per_hour)

gross_pay=hours*rate_per_hour
print(gross_pay)

f=open("C:\\Users\\YELLOW WINTERS\\Desktop\\exercise.txt","w")
print("hours: ",hours, file=f)
print("rate_per_hour:",rate_per_hour, file=f)
print("gross_pay:",gross_pay, file=f)
f.close()
