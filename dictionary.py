student={
    "names" : "Jane",
    "Reg_no" : "BSCIT-05-0000/2023",
    "DOB" : 2005
}
#update add the student email to the dictionary
student.update({"email" : "jane@gmail.com"})
print(student)

#get is used to get a certain item from the dictionary
y=student.get("names")
print(y)

#removes the last item from the dictionary
student.popitem()
print(student)


student.pop("Reg_no")
print(student)

