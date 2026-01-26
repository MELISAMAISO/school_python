#BSCIT-05-0080/2024
#MOKEIRA MAISO

import math

radius=int(input("Enter radius:"))

volume=4/3*math.pi*radius**3

print(volume)

f=open("C:\\Users\\YELLOW WINTERS\\Desktop\\volume.txt","w")
print("radius:",radius, file=f)
print("volume:",volume, file=f)
f.close()
