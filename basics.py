#BSCIT-05-0080/2024
#MOKEIRA MAISO
#python variables
f_name="John"
age=20
discount=20.35
tall=True
x,y,z="orange",10,3.142
a=b=c="James"
a=10
b=20

sum=a+b
print(sum)
print("The sum is",sum)
f = open("C:\\Users\\YELLOW WINTERS\\Desktop\\mel.txt","w")#writes to the file mel.txt
print("The sum is", file=f)
print("Name:",f_name,file=f)
f.close()

last_name=input("Enter your name:")
score=int(input("Enter marks:"))
budget=float(input("Enter budget:"))
print(last_name,score,budget)

f = open("C:\\Users\\YELLOW WINTERS\\Desktop\\mel.txt","a")#adds to the file mel.txt
print("last_name: ",last_name, file=f)
print("score:",score, file=f)
print("budget:",budget, file=f)
f.close()
