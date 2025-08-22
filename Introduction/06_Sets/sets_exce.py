#EXERCISE 

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Tesla", "Youtube"])
print(it_companies)

# Remove one of the companies from the set it_companies
print(it_companies.pop())

# Exercises: Level 2
# Join A and B

C = A.union(B)
print(C)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
D = B.union(A)
print(D)

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A, B

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(age))

age = set(age)

print(len(age)) # set is shorter due to is a UNIQUE collection of elemnts 


# I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split(" ")

unique_words = set(words)
print(unique_words)