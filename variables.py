#'Day 2:30 Days of Python programming'
first_name = "John"
last_name= "Doe"
full_name= first_name + " "+ last_name
country="USA"
city="New York" 
age=20
year=2026
is_married=False
is_true=True
is_light_on=True
  
#Declaring multiple variable
first_name,last_name,full_name,country,city ="John","Doe",{first_name + " " + last_name},"USA"," NewYork"
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
#Using len
print("First name:", len(first_name),"Second name:", len(last_name))
#operators
num_one=5
num_two=4
total=num_one+num_two
diff=num_two-num_one
remainder=num_two%num_one
exp=(num_one**num_two)
floor_division=(num_one//num_two)
print(total,diff,remainder,exp,floor_division)
#Radius of a circle
import math
radius=30
area_of_circle=math.pi*radius*radius
circum_of_circle=2*math.pi*radius
#display 
print("Area of a circle: " , area_of_circle)
print("Circumference of circle: ",circum_of_circle)
#user input
radius=float(input("Enter the radius of the circle: "))
area_of_circle=math.pi*radius*radius
print("Area of the circle =", area_of_circle)

first_name=input("Enter your first name: ")
last_name=input("Enter yout last name: ")
country=input("Enter your country: ")
age=input("Enter your age: ")

print("First Name:",first_name)
print("Last Name: ",last_name)
print("Country: ",country)
print("Age: ",age)
