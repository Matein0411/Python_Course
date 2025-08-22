# tuples in python

# Tuples are immutable sequences in Python, meaning they cannot be changed after creation.
# They are defined using parentheses () and can contain mixed data types.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (1, 2, 3, "Matein", "hi")
my_other_tuple = ("Hello", 2)

print(my_tuple)

# accessing tuple items and search for an item
print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("hi"))
print(my_tuple.index("hi"))

# my_tuple[1] = "onion" 'tuple' doesnt support item assignment

# concatenation and repetition
new_tuple = my_tuple + my_other_tuple
print(new_tuple)

# slicing
new_tuple = my_tuple[0:3]
print(new_tuple)

# mutable tuple and convert it to a list
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Monday"
my_tuple.insert(11, 23)
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# you can use len in a tuple  too
print(len(my_tuple))

# delete a tuple
del my_tuple