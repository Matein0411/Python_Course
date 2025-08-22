# dictionaries in python

# A dictorionary is a collection of unordered, modifiable (mutable) paired (key:value) data type.

# syntax

empty_dict = {}

dct = {"Key1" : "value1", "Key2" : "Value2", "Key3" : "Value3"}

# example

person = {
    "first_name" : "luchin",
    "last_name": "Yetayeh",
    "age" : 25,
    "country" : "Finland",
    "is_married": True,
    "skills": ["JS", "React", "Node", "SQL"], 
    "address" : {
        "street" : "Space street",
        "zipcode" : "02210"
    }
}
print(person["address"]["street"]) # accessing nested dictionary
print(person["skills"][0]) # accessing list inside a dictionary

# a dictionary value could be any data types

# length

print(len(person)) # 7

# Accesing dictionary items
# We can access dictionary items by referring to its key name

print("Name : " + person["first_name"] + " "+ person["last_name"])
print(person["age"]) #25

# adding items to a dictionary
person["have_pets"] = True

print(person["have_pets"])

# modifying items in a Dictionary
person["first_name"] = "Matein"

print(person["first_name"])

# checking keys in a dictionary using "in" operator
print("first_name" in person) # true
print("phone_number" in person) # false

# removing key and value pairs from a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop("key1") # removes key1 item and returns the value
dct.popitem() # removes the last item and returns the value
del dct["key2"]

# Changing dictorionary to a list of items
# items() changes to a list of tuples
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# clearing a dictionary, just removing content, not the variable
print(dct.clear())

# deleting a  dictionary
del dct

# copy a dictionary
person_copy = person.copy()

# Getting dictionary keys as a list
# the Keys() method gives us all the keys as a list

keys = person.keys()
print(keys)

# Getting dictionary values as a list
values = person.values()
print(values)