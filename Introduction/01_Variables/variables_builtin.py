# Variables in Python

my_string_variable = 'Mateo Yunga :)'
my_int_variable = 21
my_bool_variable = True

# declaring multiple variables in one line
my_float_variable, my_list_variable = 3.14, [1, 2, 3]

# cast a variable to a different type
my_int_to_str_variable = str(my_int_variable) # convert int to str
print(type(my_int_to_str_variable)) # type: str

# explicitly assign the type of a variable
my_explicit_str_variable: str = "Hello, World!"
my_explicit_int_variable: int = 42
my_explicit_float_variable: float = 3.14
my_explicit_bool_variable: bool = True

# print the values stored in the variables

print("Hi, my name is: ", my_string_variable)
print("I am: ", my_int_variable, "years old")
print("Am I a student? ", my_bool_variable)

# builtin functions

print(len(my_string_variable))  # length of the string
print(max(my_list_variable))     # maximum value in the list
print(min(my_list_variable))     # minimum value in the list
