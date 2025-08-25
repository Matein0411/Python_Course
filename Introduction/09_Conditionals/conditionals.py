# conditionals in python

# if condition:  -> Sintaxis

a = 3
if a > 0:
    print(f"{a} is a positive number")

# if-else condition:  -> Sintaxis
if a > 0:
    print(f"{a} is a positive number")
else:
    print(f"{a} is a negative number")

# if-elif-else condition:  -> Sintaxis
a = 0
if a < 0:
    print(f"{a} is a negative number")
elif a == 0:
    print(f"{a} is zero")
else:
    print(f"{a} is a positive number")

# short hand if-else condition:  -> Sintaxis
a = 3
print("a is a positive number") if a > 0 else print("a is a negative number")

# nested condition

a = 0
if a > 0:
    if a % 2 == 0:
        print("A is a positive and even integer")
    else:
        print("A is a positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")

# if condition with logical operators
a = 0
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print("A is a positive integer")
else:
    print("A us zero")

# if and or logical operators
user = "admin"
access_level = 3
if user ==  "admin" or access_level >= 4:
    print("Access granted")
else:
    print("Access denied")

# conditional with value inspection

my_String = ""
if not my_String:
    print("String is empty")

if my_String == "textttttttt":
    print("Text strings are equals")