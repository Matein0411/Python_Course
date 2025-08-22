''''
EXERCISE 
LEVEL 1 and 2 :)
'''

# create an empty tuple
family_members = ()

# creeate a tuple containing names of your sister and your brothers 
brothers = ("Ian", "Pepe") 
sisters = ("Maria", "Andrea")

# join brothers and sisters tuple and assign it to siblings
siblings =  brothers + sisters

# how many siblings do u have?
print(len(siblings))

# add father and mom
fathers = ("Marcia", "Esteban")
family_members = siblings + fathers

print(family_members)

# unpack siblings from family members again
siblings = ()
siblings = family_members[:4]
print(siblings)

# create fruits, vegetables and animal products tuples. Join the three tuples and assign 
# it to a variable called food_stuff_tp

fruits_tp = ("Apple", "Banana", "Orange", "Lemon")
vegetables_tp = ("Tomatoe", "Potato", "Onion")
animals_tp = ("Cow", "Chicken", "Fish")

food_stuff_tp = fruits_tp + vegetables_tp + animals_tp

# change  the final tuple to a list

food_stuff = list(food_stuff_tp)
print(type(food_stuff))

food_stuff = tuple(food_stuff)
# slice out the middle item or items from the tuple

mid = len(food_stuff) // 2
middle_food = food_stuff[mid-1]
if(len(food_stuff) % 2 == 0):
    middle_food += " " + food_stuff[mid]

print(middle_food)

# slice out the first three and the last three items

first_three = food_stuff[:3]
print(first_three)

last_three = food_stuff[-3:]
print(last_three)

# check if a item exists

print(food_stuff.count("Chicken"))

# delete 
del food_stuff