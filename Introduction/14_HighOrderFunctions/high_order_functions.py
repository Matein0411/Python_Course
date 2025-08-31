# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable

# function as a parameter

def sum_numbers(nums):
    return sum(nums) # abusing the built-in sum function

def high_order_function(f, lst):
    summation = f(lst)
    return summation

result = high_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result) # 15

# function as a return value

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

# if you use () at a function, youre executing the function, without ()
# you are just calling the function
def high_order_function(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute

result = high_order_function("square")
print(result(3))

# PYTHON CLOSURES

"""
Python allows a nested function to access the outer scope of the enclosing function. 
This is is known as a Closure. 
"""

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))
    
# PYTHON DECORATORS

"""
Design pattern in python that allow a user to add
new functionality to an existing object without modifying its structure.
"""

# normal function
def greeting():
    return "Welcome to python"
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g())

# now, we are using decorators

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return "Welcome to python"
print(greeting())

#multiple decorator to a single function

# first decorator

def uppercase_decorator(function):
    def wrapper():
        func =  function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# second decorator

def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator
def greeting():
    return "Welcome to Python"
print(greeting())

# accepting parameters in decorator functions

def decorator_With_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_With_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(first_name, last_name, country))

print_full_name("Mateo", "Yunga", "Ecuador")

# BUILT-IN HIGHER ORDER FUNCTIONS

# map(), takes a function and iterable parameters

nums = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2

nums_squared = map(square, nums)
print(list(nums_squared))

# lets apply it with a lambda function

nums_squared = map(lambda x : x ** 2, nums)
print(list(nums_squared))


names  = ["Mateo", "Anderson", "Micaela", "Messi", "Goku"]

def change_to_uppercase(name):
    return name.upper()

names_upper_cased = map(change_to_uppercase, names) 
print(list(names_upper_cased))

names_upper_cased = map(lambda name : name.upper(), names)
print(list(names_upper_cased))

# fylter function

"""
The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). 
It filters the items that satisfy the filtering criteria.
"""

def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_nums = filter(is_even, nums)
print(list(even_nums))

# Reduce function

"""
The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable.
 However, it does not return another iterable, instead it returns a single value.
"""
nums_str = ["1", "2", "3", "4", "5"]

def add_two_nums(x ,y):
    return int(x) + int(y)

from functools import reduce

total = reduce(add_two_nums, nums_str)
print(total)