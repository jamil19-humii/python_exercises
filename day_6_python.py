#empty tuple
empty_tuple=()
print("Empty Tuple:", empty_tuple)
print('_______________________________________________')
#tuple containing names
brothers_tuple=("John","Mike","David")
sisters_tuple=("Anna","Mary","Kate")
#joining two tuples
siblings=brothers_tuple+sisters_tuple
print("Siblings:", siblings)
#How many siblings do you have?
print('Number of siblings:', len(siblings))
print('_______________________________________________')
#modifying siblings_tuple and add the name of your father and mother and assign it to family_members
family_members=siblings+("Hillary","Ariana")
print("Family Members:", family_members)
print('________________________________________________ ')
#Unpacks siblings and parents from family_members
*siblings, father, mother=family_members
print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)
print("_______________________________________________")
#create fruits,vegetables,animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=("apple","banana","orange")
vegetables=("carrot","broccoli","spinach")
animal_products=("milk","cheese","eggs")
food_stuff_tp=fruits+vegetables+animal_products
print("Food Stuff (Tuple):", food_stuff_tp)
print("_______________________________________________")
#change the tuple food_stuff_tp to a list and assign it to a variable called food_stuff_lt.
food_stuff_lt=list(food_stuff_tp)
print("Food Stuff (List):", food_stuff_lt)
print("_______________________________________________")
#slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print("Middle Item(s) from food_stuff_tp:", food_stuff_tp[len(food_stuff_tp)//2])   
#slice out the first three items and the last three items from food_staff_lt list
print('First three items from food_stuff_lt:', food_stuff_lt[:3])
print('Last three items from food_stuff_lt:', food_stuff_lt[-3:])
print("_______________________________________________")
#Delete the food_staff_tp tuple completely
del food_stuff_tp

print('_________________________________________________')
#check if 'Estonia' is a nordic country
nordic_countries=('Denmark','Finland','Iceland','Norway','Sweden')
print("Is 'Estonia' a nordic country?", 'Estonia' in nordic_countries)
print("Is  'Iceland' a nordic country?", 'Iceland' in nordic_countries)






