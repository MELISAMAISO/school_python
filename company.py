#BSCIT-05-0080/2024
#Maiso
#decision making
salary=float(input("Enter your salary: "))
year_of_service=int(input("Enter your years of service: "))

if (year_of_service>10):
    bonus=0.1*salary
    #in python we do not use elseif instead we use elif 
    #we do not use the && we use the AND
elif(year_of_service >=6 and year_of_service <=10):
    bonus=0.08*salary
else:
    bonus=0.06*salary

print("The bonus is", bonus)   

#if using windows must escape the back slash
f= open("C:\\Users\\YELLOW WINTERS\\Desktop\\bonus.txt","a")#writes to the file bonus.txt
print("The bonus is",bonus,file=f)
print("The salary is",salary,file=f)
f.close()#always close the file

