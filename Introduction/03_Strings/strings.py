# Strings in Python

letter = "A"
print("The first letter of the alphabet is:", letter)

multiline_str = '''
This is a multi-line string.
It can span multiple lines.
'''

my_new_line_str = "This is a String\nwith new line"
print(my_new_line_str)

my_tab_str = "This is a String\twith new tab "
print(my_tab_str)

quote_str = "This is a String with \"quotes\" inside"
print(quote_str)


# concat
first_name = 'Pepe'
last_name = 'Le Pew'
print("Full name:", first_name + " " + last_name)

# Formating
name, last_name, age = "Pepe", "Le Pew", 5
print("My name is {}{} and my age is {}".format(name, last_name, age))
print("My name is %s %s and my age is %d" % (name, last_name, age)) #-> useful
print(f"My name is: {name} {last_name} {age} ") # -> useful

# Unpacking strings
language = "Python"
a,b,c,d,e,f = language
print(a)
print(e)

# Accesing characters 
print(language[1])
print(language[-1]) #last index

# Slicing
language_slice = language[1:3] #1,2 index
print(language_slice)

language_slice = language[1:] # all without first character
print("hi" + language_slice)

language_slice = language[:3] #0,1,2 index
print(language_slice)

language_slice = language[::2] # all with step 2
print(language_slice)

language_slice = language[0:6:2] # start, end, step -> index 0, 2, 4
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Bultin functions

print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count('o')) # count the number of 'o' in the string
print(language.isnumeric())
print(language.startswith("Py"))
