# loops in python

# WHILE LOOP

count = 0

while count < 5:
    print(count)
    count += 1 # print 0, 1, 2, 3, 4

# if we are interested to run block of code once the condition
# is no longer true, we can use else

count = 0

while count < 5:
    print(count)
    count += 1
else:
    print(count) # print 0, 1, 2, 3, 4, 5


# BREAK AND CONTINUE

#  Break: We use break when we like to get out of or stop the loop.

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3: # only print 0, 1, 2
        break

# Continue: With the continue statement we can skip the current iteration, and continue with the next:
count = 0

while count < 5:
    if count == 3: # print 0, 1, 2, 4, 5 -> focus on 2, 3 was skipped
        count += 1
        continue
    print(count)
    count += 1


# FOR LOOP

# Loop FOR is used for iterating over a sequence 

# with list, tuple, set, dict and strings

numbers = [1, 2, 3, 4, 5]

for number in numbers:  # number is temporary name to refer to the list's items, valid only inside this loop
    print(number) # 1, 2, 3, 4, 5

string = "Language"

for letter in string:
    print(letter) # l, e, n, g, u, a, g, e

# or

for i in range (len(string)):
    print(string[i])

# RANGE FUNCTION

"""
The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. 
The range sequence needs at least 1 argument (end)
 """

lst = list(range(0, 12, 2))
print(lst) # [0, 2, 4, 6, 8, 10, 12]

# NESTED FOR LOOP

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == "skills":
        for skill in person ["skills"]:
            print(skill)

# FOR ELSE
# If we want to execute some message when the loop ends, we use else.

for number in lst:
    print(number)
else:
    print("Numbers list completed")

# PAST
# In python when statement is required (after semicolon), but we don't like to execute any code there we can writte the word pass
for number in range(6):
    pass

