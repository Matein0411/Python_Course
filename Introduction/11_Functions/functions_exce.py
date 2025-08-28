from countries_data import countries_data

# Exercises: Level 1

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(number1, number2):
    return number1 + number2

print(add_two_numbers(4, 5))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

pi = 3.14

def calculate_circle_are(radius):
    return pi * radius * radius

print(calculate_circle_are(5))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all_nums(4, 5, 6))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_Celsius_to_farenheit(grades):
    return (grades * 9/5) + 32

print(convert_Celsius_to_farenheit(32))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

seasons = {
    "Winter" : "September"
    # and others :) jejejeje 
}

def check_season(month):
    for key, value in seasons.items():
        if month == value:
            return key

print(check_season("September"))

# Write a function called calculate_slope which return the slope of a linear equation

point_a = [3, 4]
point_b = [5, 6]

def calculate_slop(point_a, point_b):
    slope = (point_b[1] - point_a[1]) / point_b[0] - point_a[0] 
    return slope

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_cuadratic_eqn(a, b, c):
    x1 = (-b + (b ** 2 - 4 *a *c ) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 *a *c ) ** 0.5) / (2 * a)
    print(f"Solution: x1 = {x1}, x2= {x2}")

solve_cuadratic_eqn(2, 9, 10)

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

lst = [4, 2, 3]

def print_list(list: list):
    for i in list:
        print(i, end = " ")

print_list(lst)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def print_reversed_list(lst: list):
    print()
    for i in range(len(lst)-1, -1, -1):
        print(lst[i])

print_reversed_list(lst)

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

lst = ["a", "b", "v"]

def capitulize_list_items(lst: list):
    for i in lst:
        print(str(i).capitalize())

capitulize_list_items(lst)

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']

def add_item(item, lst):
    lst.append(item)
    for i in lst:
        print(i, end = " ")

add_item("Onion", food_staff)

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(lst: list, item):
    if item in lst:
        lst.remove(item)
        print(lst)
    else:
        print("Item not found")

remove_item(food_staff, "Potato")

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.


def sum_of_numbers(number):
    num = 0
    total = 0
    while num <= number:
        total += num
        num += 1
    print(total)

sum_of_numbers(5)

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odd(number):
    total = 0
    for num in range(number + 1):
        if num % 2 != 0: 
           total += num
    print(total)

sum_of_odd(5)

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(number):
    total = 0
    for num in range(number + 1):
        if num % 2 == 0: 
           total += num
    print(total)

sum_of_even(5)

# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(number):
    odds_counter = 0
    evens_counter = 0

    for num in range(number + 1):
        if num % 2 == 0:
            evens_counter += 1
        else:
            odds_counter += 1
    print(f"Sum of evens: {evens_counter}, sum of odds: {odds_counter}")

evens_and_odds(100)

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(num):
    total = 1
    if num == 0: 
        return 0
    if num == 1:
        return 1

    while num > 0:
        total *= num
        num -= 1
    
    return total

print (factorial(10))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(arg):
    if not arg:
        print("Is empty")
    else:
        print("Not empty")

is_empty("")

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

job_salaries = [45646, 13214, 56464]

def calculate_mean(lst):
    median = 0
    for i in lst:
        median += i
    median = median / len(lst)
    print(median)

calculate_mean(job_salaries)

# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.

def is_prime(num):
    count = 0
    for i in range(num, 0, -1):
        if num % i == 0:
            count += 1
    if count == 2:
        print("Is prime")
    else:
        print("Nop :(")

is_prime(67)

# Write a functions which checks if all items are unique in the list.

def items_unique(lst: list):
    if len(lst) == len(set(lst)):
        print("All elements are unique")
    else:
        print("Not unique")

items_unique([2, 1, 3])

# Write a function which checks if all the items of the list are of the same data type.

def are_the_same_type(lst: list):
    equal = True
    for i in range(0, 1):
        for j in range(1, len(lst)):
            if type(lst[i]) != type(lst[j]):
                equal = False
                break

    if equal:
        print("Equal type")
    else:
        print("Not equal")

are_the_same_type([1, 2, 3])

# Write a function which check if provided variable is a valid python variable
import keyword

def is_valid_variable(var_name):
    if not isinstance(var_name, str):
        print("Input must be a string.")
        return False
    if not var_name.isidentifier():
        print(f'"{var_name}" is not a valid identifier.')
        return False
    if keyword.iskeyword(var_name):
        print(f'"{var_name}" is a reserved keyword.')
        return False
    print(f'"{var_name}" is a valid Python variable name.')
    return True

is_valid_variable("my_var")     
is_valid_variable("2var")        # Not valid
is_valid_variable("for")         # Reserved keyword


# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order




def most_spoken_languages(dct: dict, num):
    languages = {}

    for country in dct:
        for language in country["languages"]:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1

    lst = list(languages.items())

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)): 
            if lst[i][1] < lst[j][1]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp

    print(lst[:num])

most_spoken_languages(countries_data, 10)


# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

def most_populated_countries(dct: dict, num):

    countries_pop = []
    for country in dct:
        countries_pop.append((country["name"], country["population"]))

    for i in range(len(countries_pop)):
        for j in range(i+1, len(countries_pop)):
            if countries_pop[i][1] < countries_pop[j][1]:
                temp = countries_pop[i]
                countries_pop[i] = countries_pop[j]
                countries_pop[j] =  temp
    
    print(countries_pop[:10])
most_populated_countries(countries_data, 10)