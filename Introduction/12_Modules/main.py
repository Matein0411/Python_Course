# Modules in python

"""
A module is a file containing a set of codes or a set of functions which can be
included to an app.
"""

# importing a module

import my_module

print(my_module.printValue(45))

# importing functions from a module

from my_module import sumValue, printValue

print(sumValue(4, 5, 9))

# importing functions from a module and renaming

from my_module import sumValue as sum, printValue as printer

print(sum(4, 5))

# IMPORT BULIT-IN MODULES

import os
# creating a directory

#os.mkdir("directory name")
# chaging the current directory
# os.chdir("path")

# getting current working directory
#os.getcwd()

# removing a directory
#os.rmdir()

# import sys
"""
privedes functions and variables used to manipulate different parts of 
the python runtime environment.
"""

import sys


print("Welcome {}. Enjoy {} challenge!". format(sys.argv[1], sys.argv[2]))

# try with this at the terminal: python main.py Hola Pepe
# you will see: Welcome Pepe. Enjoy Python challenge!

# statics module

"""
Provides unctions for mathematical statics of numeric data.
"""

from statistics import * # import all the statics modules

ages = [20, 18, 17, 21, 23, 29]

print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# math module

import math

print(math.pi)  # 3.14 pi constant
print(math.sqrt(2))
print(math.pow(2, 3)) # 8.0 exponencial function
print(math.floor(9.81)) # 9, rounding to the lowest
print(math.ceil(9.81)) # 10, rounding to the highest
print(math.log10(100)) # 2, logarithm with 10 as base

# string module
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# random module
from random import random, randint

print(random()) # value between 0 and 0.9999
print(randint(5, 20)) # value between [5, 20] inclusive