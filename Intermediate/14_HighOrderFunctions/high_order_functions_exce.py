from functools import reduce

# Exercises: 
countries = ['Estonia', 'Finland', 'Sweden', "England", 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

# Explain the difference between map, filter, and reduce.

"""
All of them uses a function, and a iterable item like a list, tuple, etc.
However, a map just iterates doing things 
according to the function for each iteam, a filter uses a boolean function in order
to stisfy a filtering criteria, finally a reduce function returns a single value/
"""

# Explain the difference between higher order function, closure and decorator

"""
- Higher order function: Is a functions that can receive other functions as arguements,
or return another function as a result.

- Closure: Is a inter function that can use elements of the extern function,
even if after thaf the function ends. Personalizable functions that remain a intern state.

- Decorator: Is a useful tool to adding new funciontalities to antoher function
without change the code. Is a design pattern in python.
"""

# Define a call function before map, filter or reduce, see examples.

def to_upper(item):
    return item.upper()

result = list(map(to_upper, "Hola"))
print(result)

# Use for loop to print each country in the countries list.

for country in countries:
    print(country)

# Use for to print each name in the names list.

for name in names:
    print(name)

# Use for to print each number in the numbers list.

for num in numbers:
    print(num)

# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list

def change_to_uppercase(item):
    return item.upper()

uppercase_countries = map(change_to_uppercase, countries)
print(list(uppercase_countries))

# Use map to create a new list by changing each number to its square in the numbers list

def square(num):
    return num ** 2

print(list(map(square, numbers)))  

# Use map to change each name to uppercase in the names list

print(list(map(change_to_uppercase, names)))

# Use filter to filter out countries containing 'land'.

def if_contains_land(item):
    if "land" in item:
        return True
    else:
        return False
    
print(list(filter(if_contains_land, countries)))

# Use filter to filter out countries having exactly six characters.

def has_six_letters(item):
    if len(item) == 6:
        return True
    else:
        return False
    
print(list(filter(has_six_letters, countries)))

# Use filter to filter out countries containing six letters and more in the country list.

def has_six_letters_or_more(item):
    if len(item) >= 6:
        return True
    else:
        return False
    
print(list(filter(has_six_letters_or_more, countries)))

# Use filter to filter out countries starting with an 'E'

def starts_with_e(item):
    if item.startswith("E"):
        return True
    else:
        return False
    
print(list(filter(starts_with_e, countries)))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

# map

upper_countries = map(str.upper, countries)

# filter

filtered_countries = filter(lambda x : "LAND" in x, list(upper_countries))

# reduced

reduced_countries = reduce(lambda x, y : x + "," + y, list(filtered_countries))

print(reduced_countries)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

lst = ["a", 2]

def get_string_list(lst):
    string_list = (i for i in lst if type(i) == str )
    print(list(string_list))

get_string_list(lst)

# Use reduce to sum all the numbers in the numbers list.

total = reduce(lambda x, y : x + y, numbers)
print(total)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia,
#  Finland, Sweden, Denmark, Norway, and Iceland are north European countries

european_countries =  reduce(lambda x, y: x + "," + y, countries[:-1]) + " and " + countries[-1] + " are north European countries"
print(european_countries)

# Declare a function called categorize_countries that returns a list of countries with some 
# common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).


def categorize_countries(lst):
    common_countries = [i for i in lst if "land" in i]
    return common_countries

print(categorize_countries(countries))


# Create a function returning a dictionary, where keys stand for starting letters of countries and values are 
# the number of country names starting with that letter.

def create_dict(lst):
    dct = {}

    for i in range(len(lst)):
        letter = lst[i][0]
        count = 0
        for j in range(len(lst)):
            if lst[j][0] == letter:
                count += 1
        dct[letter] = count
    return dct

print(create_dict(countries))

# Declare a get_first_ten_countries function - it returns a list of first ten 
# countries from the countries.js list in the data folder.


# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.


# Exercises: Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

# Sort countries by name, by capital, by population

# Sort out the ten most spoken languages by location.

# Sort out the ten most populated countries.