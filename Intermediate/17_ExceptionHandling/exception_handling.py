# Python Handling

"""
Python uses try and except to handle errors graceful. 
A graceful exit (or graceful handling) of errors is a simple programming 
idiom - a program detects a serious error condition and "exits gracefully", in a controlled manner as a result.
"""

try:
    print(10 + "5")
except:
    print("Something went wrong")

try:
    name = input("Enter your name: ")
    year_born = input("Year you were born: ")
    age = 2025 - year_born
    print(f"Your are {name}. And your age is {age}")
except:
    print("Something went wrong")

# In the following example, it will handle the error and will also tell us the kind of error raised.

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2025 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

# In the code above the output is going to be TypeError. Now, let's add an additional block:

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else: # no exceptions? run this code
    print('I usually run with the try block')
finally: # always run this code
    print('I always run.')

