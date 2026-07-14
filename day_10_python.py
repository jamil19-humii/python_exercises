#Loops
#iterate 0-10 using for loop&while loop
#1.for loop
for i in range(11):
    print(i)
print("________________________________________________")
#2.while loop
count=0
while count<=10:
    print(count)
    count+=1
print("_____________________________________________________")
#iterate 10-0 using for loop &while loop
#1.for loop
for i in range(10,-1,-1):
    print(i)
print("________________________________________________________")
#2.while loop
count=10
while count>=0:
    print(count)
    count-=1
print("________________________________________________________")
#loop that makes seven calls to print()   
for i in range(1,8):
    print('#'* i)
print("_____________________________________________________")

#nested loop
for row in range(7):          # 7 rows
    for col in range(8):      # 8 columns
        print("#", end=" ")   # print # without new line
    print()                   # move to next line after each row
print("________________________________________________________")
for i in range(11):   # from 0 to 10
    print(f"{i} x {i} = {i * i}")
#iterate through the list using for loops
lang_list=['Python','Numpy','Pandas','Django','Flask']
for item in lang_list:
    print(item)
print("________________________________________________________")    
#iterate from 0 to 100 using for loop and print only even numbers
print("EVEN NUMBERS")
for i in range(101):
    if i % 2==0:
        print(i)
print("__________________________________________________________")
#iterate from 0 to 100 using for loop and print only odd numbers
print("ODD NUMBERS")
for i in range(101):
  if i% 2 !=0:
      print(i)
#sum of numbers(0-100)

total=0
for i in range (101):
    total += i
print("The sum of all numbers is:",total)
print("__________________________________________________")

#print sum of all evens and odds(0-100)
#1.even
sum_even=0
for i in range(0,101,2):
    sum_even +=i
print("The sum of all even is:",sum_even)
#odd
sum_odd=0
for i in range(1,101,2):
    sum_odd += i
print("The sum of all odds is:",sum_odd)
print("_______________________________________________________")
print("Countries containing the word land\n")
from countries import countries
for country in countries:
    if "land" in country:
        print(country)
print("____________________________________________________________")

from countries_data import countries_data #countries data is a list of dicts
#i.Total number of languages in the data
unique_languages = set()#collect languages into a set to avoid duplicates
for country in countries_data:
    for lang in country['languages']:
        unique_languages.add(lang)
print("Total number of languages:",len(unique_languages))
print("_____________________________________________________________________")
#ii.Ten most spoken languages from the data
from collections import Counter
language_counter=Counter()
for country in countries_data:
    for lang in country['languages']:
        language_counter[lang]+=1
most_spoken=language_counter.most_common(10)
print("Ten most spoken languages:")
for lang,count in most_spoken:
    print(lang,"spoken in",count,"countries")
print("_________________________________________________________________________")
#iii.Find 10 most populated countries in the world
#sort countries by population(descending)
sorted_by_population=sorted(countries_data, key=lambda x: x['population'], reverse=True)
print("Ten most populated countries:")
for country in sorted_by_population[:10]:
    print(country['name'],"-",country['population'])


