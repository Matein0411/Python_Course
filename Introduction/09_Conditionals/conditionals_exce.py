
# Exercises: Level 1
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, 
# give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive")
else:
    diff = 18 - age
    print(f"you need {diff} more years to drive")

# You need 3 more years to learn to drive.
# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' 
# for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

my_age = 21
user_age = int(input("Enter your age: "))

diff = my_age - user_age

if diff == 0:
    print("We have the same age")
else:
    years = abs(diff)
    if years == 1:
        year_str = "year"
    else:
        year_str = "years"
    if diff > 0:
        print(f"I am {years} {year_str} older than you")
    else:
        print(f"You are {years} {year_str} older than me")

# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, 
# else a is equal to b. Output:

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

if num1 > num2:
    print("Num1 is greather than num2")
elif num2 == num1:
    print("Num1 is equal to num2")
else:
    print("Num1 is smaller than num2")

# Exercises: Level 2
# Write a code which gives grade to students 
# according to theirs scores:

grades = {
    "A": (80, 100),
    "B": (70, 89),
    "C": (60, 69),
    "D": (50, 59),
    "F": (0, 49)
}

score = int(input("Enter your grade"))

for grade, (min_score, max_score) in grades.items():
    if min_score <= score <= max_score:
        print(f"Your score is {grade}")

"""
Check if the season is Autumn, Winter, Spring or Summer. 
If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. 
March, April or May, the season is Spring June, July or August, the season is Summer
"""
month = str(input("Enter month: ")).lower()

seasons = {
    "Autumn" : ("september", "october", "november"),
    "Winter" : ("december", "january" , "february"),
    "Spring": ("april", "may"),
    "Summer": ("july", "august")
}

for season, months in seasons.items():
    if month in months:
        print(f"The season of the month is {season}")
        break
else:
    print("Invalid month")

# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')

new_fruit = str(input("Enter a fruit: ")).lower()

if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print(f"New list of fruits: {fruits}")

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'is_married': True,
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if "skills" not in person:
    print("Person does'nt have skills")
else:
    middle_skill = person["skills"][int(len(person["skills"])/2)]
    print(middle_skill)

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if "skills" not in person:
    print("Person does'nt have skills")
elif "Python" in person["skills"]:
    print("Person has python skill")

"""
  * If a person skills has only JavaScript and React, print('He is a front end developer'),
    if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
    if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
    else print('unknown title') - for more accurate results more conditions can be nested!
"""
backend_skills = ["Node", "MongoDB", "Python"]
front_end_skills = ["JavaScript", "React"]

if "skills" not in person:
    print("Person does'nt have skills")
elif all(skill in person["skills"] for skill in backend_skills) and all(skill in person["skills"] for skill in front_end_skills):
    print("He is a fullStack developer")
elif all(skill in person["skills"] for skill in backend_skills):
    print("He is a backend developer")
elif all(skill in person["skills"] for skill in front_end_skills):
    print("He is a frontend developer")
else:
    print("unknown title")

#  * If the person is married and if he lives in Finland

if person["is_married"] and person["country"] == "Finland":
    print(person["first_name"] + " " + person["last_name"] + " " + "lives in Finland and is married.")
