# list comprehension

"""
List Comprehension is a compact way of creating a 
list from a sequence.
"""

# one way
language = "Python"
lst = list(language)
print(type(lst)) # list
print(lst) # ["P", "y", "t", "h", "o", "n"]

# second way: list comprehension

lst = [i for i in language]
print(type(lst)) # list
print(lst)

# more examples
numbers = [i for i in range(11)] # from o to 10
print(numbers)

squares = [ i * i for i in range(11)] 
print(squares) # [0, 1, 4, 9, 25 ...]

# list of tuples
numbers = [(i, i*i) for i in range(11)]
print(numbers) #[(0, 0), (1, 1), (2,4), (3,9) ...]

# combined with if expression

even_numbers = [i for i in range(21) if  i % 2 == 0]
print(even_numbers)

numbers = [-7, 2, -3, 1, -5, -6, 9]
positive_even_numbers = [i for i in numbers if i%2 == 0 and i > 0]
print(positive_even_numbers)

# flattering a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

# LAMBDA FUNCTION

# is a small anonymus function without a name. It can take any number of arguments, but can only
# have one expression.

# named functions
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3)) #5

add_two_nums = lambda a, b : a + b
print(add_two_nums(2, 3))

# self invoking lambda function
print((lambda a, b: a + b)(2, 3)) # 5

square = lambda x : x ** 2
print(square(3))

# multiple variables
multiple_variable = lambda a, b, c: a **2 -3 *b +4 * c
print(multiple_variable(5, 5, 3))

# lambda function inside another function

def power(x):
    return lambda n : x ** n # function power now need 2 arguments to run, in separate rounded brackets

cube = power(2)(3)
print(cube)

two_power_of_five = power(2)(5)
print(two_power_of_five)
