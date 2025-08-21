# lists in pyhton

# definition

my_list = list()  # empty list
my_other_list = []

print(len(my_list))

my_list = [1, 2, 3, 4, 5]  
my_other_list = [27, 170, "Mateo", 67.45 ]

print(len(my_list))

# accessing elements

print(my_list[0])
print(my_list[1])
print(my_list[-1]) # accessing the last element
print(my_list.count(1))  # count occurrences of 1 in the list

print(my_list.index(2))

age, height, name, weight = my_other_list
print(age, height, name, weight)

# slicing items
fruits = ["apple", "banana", "orange", "mango"]
last_fruit = fruits[-1]
all_fruits = fruits[0:4] 
all_fruits_from_second = fruits[1:] # starting from the second item
all_fruits_to_second = fruits[:2] # up to the second item (not including it)
all_fruits_with_step = fruits[::2]  # every second fruit

# modifying items
fruits[0] = "kiwi"
print(fruits)

# checking items
is_apple_in_fruits = "apple" in fruits
print(is_apple_in_fruits) # False, we already changed the value of the first element

# appending items
fruits.append("pineapple") # ["kiwi", "banana", "orange", "mango", "pineapple"]
print(fruits)

# inserting items
fruits.insert(2, "strawberry") # insert strawberry in the third position (index 2) ["kiwi", "banana", "strawberry", "orange", "mango", "pineapple"]
print(fruits)

# removing items
fruits.remove("banana") # ["kiwi", "strawberry", "orange", "mango", "pineapple"]
print(fruits)

# popping items
fruits.pop() # removes the last item ["kiwi", "strawberry", "orange", "mango"]
print(fruits)

fruits.pop(0) # removes the first item ["strawberry", "orange", "mango"]
print(fruits)

# delete items
fruits = ["banana", "apple", "pineapple"]
del fruits[0] # removes the first item ["apple", "pineapple"]
print(fruits)

# clearing items
fruits.clear() 
print(fruits) # []

# operations

my_new_list = my_list.copy()

my_new_list.extend([6, 7, 8]) # [1, 2, 3, 4, 5, 6, 7, 8]
print(my_new_list)
my_new_list.reverse() # [8, 7, 6, 5, 4, 3, 2, 1]
print(my_new_list)
my_new_list.sort() # [1, 2, 3, 4, 5, 6, 7, 8]
print(my_new_list)

# joining lists
combined_list = my_list + my_new_list
print(combined_list)
# you can also use the extend() method too :)
my_list.extend(my_new_list)
print(my_list)
