#prompting user for their age
print("AGE CHECK:")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    years_to_wait = 18 -age
    print(f"You need to wait {years_to_wait}more years to drive.")

print("\n")
#Compare the values of my_age and your_age
print("COMPARING AGES:") 
my_age= 25
your_age=int(input("Enter your age: "))
if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference ==1:
        print(f"I am {age_difference} year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
    
elif my_age < your_age:
        age_difference = your_age - my_age
        if age_difference == 1:
            print(f"You are {age_difference} year older than me.")
        else:
            print(f"You are {age_difference} years older than me.")
else:
            print("We are the same age.")

print("\n")
#prompting usser for two numbers to comapare which is greater
print("COMPARING TWO NUMBERS:")
num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))
if num1>num2:
    print(f"{num1} is greater than {num2}.")
elif num1<num2:
    print(f"{num2} is greater than {num1}.")
else:
    print(f"{num1} and {num2} are equal.")
print("\n")

#code to give students their grades based on their scores
print("GRADE CHECK:")
score = int(input("Enter your score: "))
if score >= 80:
    print("You got an A.")
elif score >= 70:
    print("You got a B.")
elif score >= 60:
    print("You got a C.")
elif score >= 50:
    print("You got a D.")
else:
    print("You got an F.")
print("\n")
##prompting the user for a month and checking the season
print("SEASON CHECK:")
month = input("Enter the month: ").strip().capitalize() #normalize input to handle case sensitivity and whitespace
if month in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
        print("The season is Spring.")
else:
    print("The season is Summer.")
print("\n")
