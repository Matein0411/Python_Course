# functions in python

# a functions is a reusable block of code or programming statements designed 
# to perform a certain task.

# SYNTAXIS
 
def my_function():
    print("Hi, im a function")

# calling a function

my_function()

# FUNCTIONS WITHOUT PARAMETERS

def generate_full_name ():
    first_name = "Mateo"
    last_name = "Yunga"
    full_name = first_name + " " + last_name
    print(full_name)

generate_full_name()

# FUNCTION WITH PARAMETERS AND RETURNING  A VALUE

def sum_two_values(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

# catching the result

my_result = sum_two_values(3, 4)
print(my_result) 

print(sum_two_values(3, 4))

# PASSING ARGUMENTS WITH KEY AND VALUE

def print_name(first_name, last_name):
    print(f"{first_name} {last_name}")

print_name(first_name="Lucho", last_name="Gonza")

# argue by default

def print_name_by_default(first_name, last_name, alias = "no alias"):
    print(f"{first_name} {last_name} {alias}")

print_name_by_default("Mateo", "Yunga")
print_name_by_default("Mateo", "Yunga", "Gol")

# ARBITRARY NUMBER OF ARGUMENTS

def summ_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(summ_all_nums(2, 3, 5))

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i, end = " ")
print(generate_groups("Team 1", "Pepe", "Lucho"))

# FUNCTIONS AS A PARAMETER OF ANOTHER FUNCTION

def square_number (n):
    return n * n
def do_something(f, x):
    return(f(x))

print(do_something(square_number, 2))