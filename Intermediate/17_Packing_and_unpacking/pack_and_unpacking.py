# Packing

# We can use the packing method to allow our function to take ultimited or arbitrary number of arguments.

# Packing lists
def summ_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(summ_all(1, 2, 3))
print(summ_all(1, 2, 3, 4))

# Packing dictionaries
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    #print(type(kwargs))
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name = "Mateo",
                          country = "Ecu", city = "Gye",
                          age = 233))

# Spreading in Python

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst) # [0, 1, 2, 3, 4, 5, 6 ,7]

# Enumerate

# We use enumarete built-in function to get the index of each item in the list

for index, item in enumerate([20, 30, 40]):
    print(index, item)

# for index, i in enumerate(countries):
#     print("hi")
#     if i == "Finland":
#         print(f"The country {i} has been found at index {index}")

# Zip

# to combine lists when looping through them

fruits = ["banana", "apple", "mango"]
vegetables = ["Tomato", "Potato", "Onion"]
fruits_and_veges = []

for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({"fuit": f, "veg":v})

print(fruits_and_veges)