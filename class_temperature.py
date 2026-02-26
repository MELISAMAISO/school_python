#python program to create a class temperature that has two methods convertFahrenheit convertCelsius

class Temperature:
    def __init__(self,celsius,fahrenheit):
        self.celsius=celsius
        self.fahrenheit=fahrenheit

    def convertFahrenheit(self):
        return(self.celsius*9/5)+32

    def convertCelsius(self):
        return(self.fahrenheit-32)*5/9
    
my_temp=Temperature(25,77)
print(my_temp.convertFahrenheit()) 
print(my_temp.convertCelsius())

#python program to create a class Circle initialize with radius and has two metods area and circumference
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius**2
    
    def circumference(self):
        return 2*math.pi*self.radius
    
my_circle=Circle(4)   
print(my_circle.area())
print(my_circle.circumference()) 


        