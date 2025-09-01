# Python error types
from math import pi
import math
# Let us the most common error types one by one.

# SyntaxError
# uncomment to see the error

#print "Hi friends"

# NameError
language = "Spanish" # comment to see the error 
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
# print(my_list[5]) # uncomment to se the error

# ModuleNotFoundError
# import maths # uncomment to see the error

# AttributeError
print(math.pi)
# print(math.PI) # uncomment to see the error

# KeyError
my_dict = {"Name" : "Mateo", "Last_name" : "Yunga"}
# print(my_dict["address"]) # uncomment to see the error

# TypeError
print(my_list[False])
# print(my_list["0"]) # uncomment to see the error

# ImportError
# from math import PI # unccoment to see the error
print(pi)

# ValueError
# my_int = int("10 years") # uncomment to see the error
my_int = int("10")
print(type(my_int))

# ZeroDivisionCero
# print(4/0) # Uncomment to see the error