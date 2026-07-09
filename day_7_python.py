# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#find the length of the set it_companies    
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add('Twitter')
#Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat', 'Pinterest'])
#remove one of the companies from the set it_companies
it_companies.remove('IBM')
print(it_companies)
#what is the difference between remove and discard?
# remove raises an error if the element is not found
# discard does not raise an error if the element is not found
it_companies.discard('IBM')  # This will not raise an error even if 'IBM' is not in the set 
print('______________________________________________________________')
#Join A and B
C=A.union(B)
print("Union of A and B:", C)
print("\n")
#Find A intersection B
intersection=A.intersection(B)
print("Intersection of A and B:", intersection)
print("\n")
#Is A subset of B
is_subset=A.issubset(B)
print("Is A a subset of B?", is_subset)
print("\n")
#Are A and B disjoint sets
are_disjoint=A.isdisjoint(B)
print("Are A and B disjoint sets?", are_disjoint)
#JOIN A WITH B AND B WITH A
A_B=A.union(B)
B_A=B.union(A)
print("A joined with B:", A_B)
print("B joined with A:", B_A)
print("\n")
#what is the symmetric difference between A and B
symmetric_difference=A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference)
print("\n")
#delete the sets completely
del A
del B
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set=set(age)
print("Length of age list:", len(age))
print("Length of age set:", len(age_set))
print("Is the age list bigger than the age set?", len(age) > len(age_set))
print
#difference between string,list,tuple and set
#String: A string is an ordered collection of characters enclosed in single or double quotes. It is immutable, meaning its content cannot be changed after creation. Strings support indexing and slicing.
#List: A list is an ordered collection of elements enclosed in square brackets. It is mutable, meaning its content can be changed after creation. Lists support indexing, slicing, and various methods for adding, removing, and modifying elements.
#Tuple: A tuple is an ordered collection of elements enclosed in parentheses. It is immutable, meaning its content cannot be changed after creation. Tuples support indexing and slicing.
#Set: A set is an unordered collection of unique elements enclosed in curly braces. It is mutable, meaning its content can be changed after creation. Sets do not support indexing or slicing, but they provide methods for set operations like union, intersection, and difference.
string_example = "Hello, World!"
list_example=[1,2,3,4,5]
tuple_example=(1,2,3,4,5)
set_example={1,2,3,4,5}
print("String Example:", string_example)
print("List Example:", list_example)
print("Tuple Example:", tuple_example)
print("Set Example:", set_example)
print("__________________________________________________________")
#Using split method and set to get the unique words in the sentence
sentence = "I am a teacher and I love to inspire and teach people"
words=sentence.split()
unique_words=set(words)
print("Unique words:", unique_words)   
   