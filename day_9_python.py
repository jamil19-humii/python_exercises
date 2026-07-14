#Conditions
# #prompting user for their age
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

#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_check = input("Enter a fruit to check: ").strip().lower() #normalize
if fruit_to_check in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit_to_check)
    print("Modified list of fruits:", fruits)
print("\n")
#Modification of person dict
person={
     'first_name':'Asabeneh',
     'last_name':'Yetahey',
     'age': 25,
     'country':'DRC',
     'is_married':'False',
     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
     'address':{
          'street': 'Space street',
          'zipcode': '02210'
     }

}
#check if the person dictionary has skills, if so print out the middle skill in the skills list
if 'skills' in person:
     skills=person['skills']
     middle_index=len(skills)//2
     print("Middle skill:", skills[middle_index])
#2.Check if 'Python is in skills
if 'skills' in person:
     has_python='Python' in person['skills']
     print("Has python Python skill:",has_python)
#3.Determine developer type
if 'skills' in person:
     skills=person['skills']
     if set(skills)=={'JavaScript','React'}:
      print("He is a front end developer")    
     elif {'Node','Python','MongoDB'}.issubset(skills):
      print("He is a backend developer.")
     elif {'React','Node','MongoDB'}.issubset(skills):
      print("He is a fullstack developer")
     else:
       print("Unknown title")
#5.Determine if the prson s married and the country they live in
if person['is_married']and person['country']=='DRC':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}.")
