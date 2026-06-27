age=21
height=5.75
complex_num=1+3j
#calculating area of triangle
base=int(input("Enter base: "))
height=int(input("Enter height: "))
area=base*height/2
print("Area of triangle: ",area)
#Calculate the perimeter of the triangle
side_a=int(input("Enter side a: "))
side_b=int(input("Enter side b: "))
side_c=int(input("Enter side c: "))
perimeter=side_a+side_b+side_c
print("Perimeter of triangle: ",perimeter)
#Area of a circle
import math
PI=3.14
radius=int(input("Enter radius: "))
area=PI*radius*radius
print("Area of circle: ",area)
circum_of_circle=2*PI*radius
print("Circumference of circle: ",circum_of_circle)

#8.calculate the slope
slope=2
y_intercept=-2
x_intercept=1
print("Slope: ",slope)
print ("Y-intercept: (0",y_intercept, ")")
print("X-intercept: (",x_intercept, ",0)")

#9.Slope & Euclidean distance between two points
x1,y1=(2,2)
x2,y2=(6,10)
slope=(y2-y1)/(x2-x1)
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Slope: ",slope)
print("Euclidean distance: ",distance)

#10.Compare 
slope_task8 = 2  

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_task9 = (y2 - y1) / (x2 - x1)


print("Slope from Task 8:", slope_task8)
print("Slope from Task 9:", slope_task9)

if slope_task8 == slope_task9:
    print("Both slopes are equal.")
else:
    print("The slopes are different.")

# Equation: y = x^2 + 6x + 9
for x in [-5, -3, 0, 2]:
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")

a, b, c = 1, 6, 9
discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Roots where y = 0:", root1, root2)
else:
    print("No real roots, discriminant < 0")

#lENGTH OF 'PYTHON' AND 'DRAGON' AND COMPARING LENGTHS
Word1 = "Python"
Word2 = "Dragon"
length_word1 = len(Word1)
length_word2 = len(Word2)
print("Length of 'Python':", length_word1)
print("Length of 'Dragon':", length_word2)
comparison = length_word1 !=length_word2
print("Are the lengths of 'Python' and 'Dragon' different?", comparison)
#in operator
sentence = "I hope this course is not full of jargon."
is_in="jargon" in sentence
print("Is 'jargon' in the sentence?", is_in)
#on operator
word = "Python" + "Dragon"
is_on="on" in word
print("Is 'on' in the word?", is_on)

#length of 'python' and convert to float&string
word=len("Python")
print("Length of 'Python':", word)
float_word=float(word)
print("Length of 'Python' as float:", float_word)
string_word=str(word)
print("Length of 'Python' as string:", string_word)

#even number check
number = 10
if number % 2==0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")

#check floor division
floor_div=7//3
#check if floor division is equal to int conversion 2.7
int_value=int(2.7)
print("Floor division of 7//3:", floor_div)
print("Int conversion of 2.7:", int_value)
print("Is floor division equal to int conversion?", floor_div == int_value)

#check if type of '10' is equal to 10
a='10'
b=10
print("Type of '10':", type(a))
print("Type of 10:", type(b))
print("Are they of the same type?", type(a) == type(b))

#prompts user to enter hours and rate per hour to calculate weekly earning
hours=float(input("Enter hours: "))
rate_per_hour=float(input("Enter rate per hour: "))
weekly_earning=hours*rate_per_hour
print("Your weekly earning is: $", weekly_earning)

#prompts user to enter number of years and calculate total seconds lived
years=int(input("Enter number of years you have lived: "))
total_seconds=years*365*24*60*60
print("You have lived for", total_seconds, "seconds.")

#script displaying table
print("Table of values:")
for i in range(1, 6):
     print(i,1,i,i**2,i**3)
