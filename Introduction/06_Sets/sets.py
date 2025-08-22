# sets in Python

# A set is an unordered and un-indexed collection of unique elements.

# sintaxis
st = set()

# creating a set with elements
st = {1, 2, 3, 4, 5}

print(len(st))

# Accesing elements
# Sets do not support indexing, slicing, or other sequence-like behavior.

print("Does set contain 3?", 3 in st)

# Adding elements
st.add(6)

# updating a set
# You can add multiple elements using the update() method.
st.update([7, 8, 9]) 

# removing elements
st.remove(2)  

# pop removes and returns an arbitrary element from the set.
removed_element = st.pop()

print(f"element removed: {removed_element}")

# clearing items in a set
st.clear() # empty set

# deleting a set
del st

# converting list to a set
lst = [1, 2, 3]
st = set(lst)

# joining sets
st1 = {1, 2, 3}
st2 = {4, 5, 6}

st3 = st1.union(st2)
print(st3)

st1.update(st2)
print(st1)

# finding intersection items

st1 = {1 ,2, 3}
st2 = {2, 4, 6}
print(st1.intersection(st2))

# checking subset and super set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
even_numbers = {2, 4, 6, 8, 10}
print(even_numbers.issubset(whole_numbers))
print(whole_numbers.issuperset(even_numbers))

# checking the difference between two sets
print(even_numbers.difference(whole_numbers)) # 10

print(whole_numbers.difference(even_numbers)) # 0, 1, 3, 5, 7, 9

# finding symmetic diffence between two seets
# it returns that it returns a set that contains all tems from both sets, except items that are present in both sets :)
# thats why both gives the same result

print(even_numbers.symmetric_difference(whole_numbers))
print(whole_numbers.symmetric_difference(even_numbers))

# joining sets
'''
If two sets do not have a common item or items we call them disjoint set. We can check if two sets are joint or
dijoint using isdisjoing() method
'''

print(even_numbers.isdisjoint(whole_numbers))