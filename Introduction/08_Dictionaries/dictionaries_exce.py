# EXERCISE

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name" : "Chispitas",
    "color" : "black",
    "breed" : "unknow",
    "legs" : "unknow",
    "age" : 2
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name" : "Andrea",
    "last_name" : "Guayas",
    "gender" : "female",
    "age" : 21,
    "marital_status" : "single",
    "skills" : ["Excell pro", "C1 English"],
    "country" : "ECU",
    "address" : {
        "city" : "Quito",
        "street" : "Juan de Benalcazar"
    }
}


# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student["skills"])

print(type(student["skills"]))

# Modify the skills values by adding one or two skills
student["skills"].append("Python")
print(student["skills"])


# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
del student["first_name"]

# Delete one of the dictionaries
del student