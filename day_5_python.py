#empty list
emlst=list()
print("Empty list:", emlst)
#list with more than 5 items
mlst=[1,2,3,4,5,6]
print("List with more than 5 items:", mlst)
print("Length of the list:", len(mlst))
#Get the first item, the middle item and the last item of the list
first_item=mlst[0]
middle_item=mlst[len(mlst)//2]
last_item=mlst[-1]
print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)
print('------------------------------')
#list with mixed data types(name, age, height, marital status, address
mixed_data_types=['Albert',30,5.9,True,'123 Main St']
print("Mixed data types list:", mixed_data_types)
print('----------------------------------------------')
#Create a list of IT companies
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print("List of IT companies:", it_companies)
print("Number of IT companies:", len(it_companies))
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies)//2])
print("Last company:", it_companies[-1])
#modify one of the companies and print the modified list
it_companies[0]='Meta'
print("Modified list of IT companies:", it_companies)
#Add company to the list
it_companies.insert(2,'Twitter')
print(it_companies)
print('\n')
#Insert a company in the middle 
middle_index=len(it_companies)//2
it_companies.insert(middle_index,"Netflix")
print(it_companies)
print('\n')
#Change Facebook to upercase
it_companies[0]=it_companies[0].upper()
print(it_companies)
print('\n')
#Join IT Companies with Hash
print("Joined It Companies using #:", '#'.join(it_companies))
print('\n')
#check if certain company exits
does_exist='Meta' in it_companies
print(does_exist)
print('---------------------------------------')
#sort list
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
print('-----------------------------------------')
#slicing
first_three=it_companies[:3]
print("Slice out first three companies from the list:",first_three)
last_three=it_companies[-3:]
print("Slice out last companies from the list: ",last_three)
middle_index=len(it_companies)//2
if len(it_companies)%2==0:
    middle_companies=it_companies[middle_index-1:middle_index+1]
else:
    middle_companies=it_companies[middle_index]
print("Slice out middle company from the list:",middle_companies)
print("----------------------------------")
#Removing companies from the list
print("Remove the first company from the list:",it_companies.pop(0))
print("Remove the last company from the list:",it_companies.pop(-1))
print("Remove the middle company from the list:",it_companies.pop(middle_index )) 
print("Remove all companies from the list:",it_companies.clear())
print("---------------------------------------------------")
#Destroy the list of IT companies

del it_companies

print("---------------------------------------------------")
#Join lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack= front_end+back_end
print("Full stack:",full_stack)
#insert 'Python' and 'SQL' after 'Redux'
full_stack.insert(full_stack.index('Redux')+1,'Python')
full_stack.insert(full_stack.index('Python')+1,'SQL')
print("Full stack after inserting Python and SQL:",full_stack)
print("---------------------------------------------------")
#List of 10 students ages
ages=[19,22,19,24,20,25,26,24,25,24]
#sort the list and find the min and max age
ages.sort()
print("Sorted ages:",ages)
min_age=ages[0]
max_age=ages[-1]
print("Minimum age:",min_age)
print("Maximum age:",max_age)
#median age
if len(ages)%2==0:
    median_age=(ages[len(ages)//2-1]+ages[len(ages)//2])/2
else:
    median_age=ages[len(ages)//2]
print("Median age:",median_age) 
#average age
average_age=sum(ages)/len(ages)
print("Average age:",average_age)   
#range of the ages
age_range=max_age-min_age
print("Range of ages:",age_range)
#compare the value of (min - average) and (max - average), use abs() method
min_avg_diff=abs(min_age-average_age)
max_avg_diff=abs(max_age-average_age)
print("Difference between minimum age and average age:",min_avg_diff)
print("Difference between maximum age and average age:",max_avg_diff)
print("---------------------------------------------------")
#list of countries
countries=['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

