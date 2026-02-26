#BSCIT-05-0080/2024
#Maiso
#prompt the user to enter marks for 3 subjects
#compute the average
#print score
subject_1 = int(input("Enter the marks of subject 1: "))
while subject_1 < 0 or subject_1 > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
    subject_1 = int(input("Enter the marks of subject 1: "))

subject_2 = int(input("Enter the marks of subject 2: "))
while subject_2 < 0 or subject_2 > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
    subject_2 = int(input("Enter the marks of subject 2: "))

subject_3 = int(input("Enter the marks of subject 3: "))
while subject_3 < 0 or subject_3 > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
    subject_3 = int(input("Enter the marks of subject 3: "))
    
average = (subject_1 + subject_2 + subject_3) / 3
print(f"Average is {average:.2f}")

if (average>70):
    score="A"
elif(average >=60):
    score="B"
elif(average >=50):
    score="C"
elif(average >=40):
    score="D"        
else:
    score="Fail"

print(score)  

f= open("C:\\Users\\YELLOW WINTERS\\Desktop\\grade.txt","a")#writes to the file bonus.txt
print("The average is",average,file=f)
print("The score is",score,file=f)
f.close()#always close the file

