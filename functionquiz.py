#create a functiom to calculate the volume of a:
#cylinder
#grading system
#volume=pi*r**2*height

import math

radius=float(input("Enter the radius of the cylinder: "))
height=float(input("Enter the height of the cylinder: "))

def volume(radius,height):
    volume=math.pi*math.pow(radius,2)*height
    return volume
print(volume(radius,height))

#grading system
score1=int(input("Enter the first subject: "))
score2=int(input("Enter the second subject: "))
score3=int(input("Enter the third subject: "))

total=score1+score2+score3
score=total/3
def grade(score):
    if score>=70:
        return"A"
    elif score>=60:
        return "B"
    elif score>=50:
        return "C"
    elif score>=40:
        return "D"
    else:
        return "FAIL"
    
print (grade(score))    