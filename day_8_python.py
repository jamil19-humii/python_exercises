#create an empty dictionary
dog={}
#add features to the dict
dog={
    'name' : 'Buddy',
    'color' : 'Brown',
    'breed' : 'Labrador',
    'legs' : 4,
    'age' : 3
}
print("Dog Dictionary:", dog)
print('_________________________________________________')
#create student dict and add features
student={
    'first_name' : 'John',
    'last_name' : 'Doe',
    'gender' : 'Male',
    'age' : 20,
    'marital_status' : 'Single',
    'skills' : ['Python', 'Java', 'C++'],
    'country' : 'USA',
    'city' : 'New York',
    'address':{
        'street' : '123 Main St',
        'zip_code' : '10001'
    }
}
#get the length of the student dict
print("Length of Student Dictionary:", len(student))
#value of skills and check the data type
print("Skills:", student['skills'])
print("Data type of skills:", type(student['skills']))
#modify the skills by adding one or two skills
student['skills'].append('JavaScript')
student['skills'].append('HTML')
print("Updated Skills:", student['skills'])
