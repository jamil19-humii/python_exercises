#concatenate strings
word1='Thirty'
word2='Days'
word3='Of'
word4='Python'
sentence=word1+' '+word2+' '+word3+' '+word4
print(sentence)
print('------------------------------')
word1='Coding'
word2='For'
word3='All'
sentence=word1+' '+word2+' '+word3
print(sentence)
company='Coding For All'
print(company)
print(len(company))
print('------------------------------')
#uppercase
print(company.upper())
#lowercase
print(company.lower())
print('------------------------------')
#using capitalize(),title(),swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())
#slice out the first word in the variable company
first_word=company.split()[0]
print(first_word)
print('                         ')
#check if 'Coding' is in the variable company using method index,find()
print(company.index('Coding'))
print(company.find('Coding'))
if company.find('Coding') != -1:
    print("'Coding' is found in the variable company.")
else:
    print("'Coding' is not found in the variable company.")
print('------------------------------')
#replace 'Coding' with 'Python'in the variable company
print(company.replace('Coding','Python'))
print('------------------------------')
#change Python for Everyone to Python for All using replace() method or other methods
company2='Python for Everyone'
print(company2.replace('Everyone','All'))
print('------------------------------')
#split the string 'Coding For All' using split() method
print(company.split())
print('------------------------------')
tech_companies='Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon'
print(tech_companies.split(','))
print('------------------------------')
print('Certain indexes in the string "Coding For All":')
#character at index 0 in the variable company
print(company[0])
#character at index 10 in the variable company
print(company[10])
#character at the last index in the variable company
print(company[-1])
print('------------------------------')
#create an acronym or abbreviation for the name  'Coding For All' & 'Python For Everyone'
phrase1='Coding For All'
acronym1=''.join(word[0] for word in phrase1.split())
print("Acronym for 'Coding For All':", acronym1)
print("    ")
phrase2='Python For Everyone'
acronym2=''.join(word[0] for word in phrase2.split())
print("Acronym for 'Python For Everyone':", acronym2)
print('------------------------------')
#using index to determine the position of letters occuring in Coding for All
print("Index of 'C' in 'Coding For All':", company.index('C'))
print("Index of 'F' in 'Coding For All':", company.index('F'))
print('----------------------------------------------')
#use rfind() to determine the position of the last occurrence of 'l' in 'Coding For All'
print("Last occurrence of 'l' in 'Coding For All':", company.rfind('l'))
#find the index of because
sentence2='You cannot end a sentence with because because because is a conjunction'
print("Index of 'because' in 'You cannot end a sentence with because because because is a conjunction':", sentence2.index('because'))
#USE Rindex to find last occurrence of 'because' in the sentence
print("Last occurrence of 'because' in the sentence:", sentence2.rindex('because'))
print('--------------------------------------------------------------')
#slice out the phrase 'because because because' in the sentence
print("Sliced phrase 'because because because':", sentence2[31:54])
#does coding for all start with a substring 'Coding'?
print("Does 'Coding For All' start with 'Coding'?", company.startswith('Coding'))
#does coding for all end with a substring 'Coding'?
print("Does 'Coding For All' end with 'Coding'?", company.endswith('Coding'))
print('--------------------------------------------------------------')
#remove the whitespace characters from the start and end of the string '   Coding For All      '
text_with_whitespace='   Coding For All      '
print("String with whitespace removed:", text_with_whitespace.strip())
print('--------------------------------------------------------------')
#variables returning boolean values using isidentifier() method
identifier1='30DaysOfPython'
identifier2='thirty_days_of_python'
print("Is '30DaysOfPython' a valid identifier?", identifier1.isidentifier())
print("Is 'thirty_days_of_python' a valid identifier?", identifier2.isidentifier())
print('--------------------------------------------------------------')
#Join the list ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] with a hash character '#'
frameworks=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("Joined frameworks:", '#'.join(frameworks))
#use new line escape to separate the following sentences
print("I am enjoying this challenge.\n I just wonder what is next.")
#use tab sequenceto write the following sentences
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
print('--------------------------------------------------------------')
#use string formatting to display the following
radius=10
area=3.14*radius**2
print(f"The area of a circle with radius{radius} is {area} meters square.")
print('\n ')
a=8
b=6
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}%{b}={a%b}')
print(f'{a}//{b}={a//b}')
print(f'{a}**{b}={a**b}')





