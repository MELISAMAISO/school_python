from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary

    def display_info(self):
        return f"The Employee Name is:{self.__name}"
    
    def get_salary(self):
        return self.__salary
    
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return super().get_salary()
        
    
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        sal=super().get_salary()*0.5
        return sal
    
emp1=FullTimeEmployee("John",10000)
emp2=PartTimeEmployee("Mary",10000)

#creating a list
employees=[emp1,emp2]

for emp in employees:
    print(emp.display_info())
    print("The Employee Salary is: ", emp.calculate_salary())
 
    
        
