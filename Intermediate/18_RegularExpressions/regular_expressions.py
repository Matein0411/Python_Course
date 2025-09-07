# Regular Expressions

# A regular expression or RegEx is a special text string that helps to find patterns in data.

import re

# after importing the re module, we can use its methods to find patterns in strings.

"""
re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string

"""

# SPAN
  
txt = "I love eating pizza"
match = re.match("I love", txt, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore

print(match)

# we can get the starting and ending position of the math as tuple using span

span = match.span()
print(span)

start, end = span
print(start, end)

substring = txt[start:end]
print(substring)

# SEARCH

txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

match = re.search("first", txt, re.I)
print(match)

span = match.span()
print(span)

start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

# SEARCHING FOR ALL MATHCES USING FINDALL

txt  = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

# it returns a list of all the matches
matches = re.findall("language", txt, re.I)
print(matches)


matches = re.findall("Python|python", txt)
print(matches)
#
matches = re.findall("[Pp]ython", txt)
print(matches)

# REPLACING A SUSTRING

match_replaced = re.sub("Python|python", "Javascript", txt, re.I)
print(match_replaced)
# or
match_replaced = re.sub("[Pp]ython", "Javascript", txt, re.I)
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

match_replaced  =  re.sub("%", "", txt)
print(match_replaced)

# SPLITTING TEXT USING REGEX SPLIT 

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split("\n", txt))

# WRITTING REGEX PATTERNS

regex_pattern = r"apple"
txt = "Apple and banana are fruits. An old cliche says an apple a day keeps the doctor away." 
matches = re.findall(regex_pattern, txt)
print(matches) # ["apple"]

# to  make case insensitive we use re.I
matches = re.findall(regex_pattern, txt, re.I)
print(matches) # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r"[Aa]pple"
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'apple']

# SQUARE BRACKET

regex_pattern = r"[Aa]pple"
txt = "Apple and banana are fruits. An old cliche says an apple a day keeps the doctor away." 
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'apple']"

# if we eant to look for the banana, we can use the or operator |
regex_pattern = r"[Aa]pple|[Bb]anana"
txt = "Apple and banana are fruits. An old cliche says an apple a day keeps the doctor away."
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'banana', 'apple']

# ESCAPE CHARACTER IN REGEX

regex_pattern = r"\d" # d is a special character which means digits
txt = "This regular expression example was made in January 12, 2020."
matches = re.findall(regex_pattern, txt)
print(matches) # ['1', '2', '2', '0', '2', '0']

regex_pattern = r"\d+"
matches = re.findall(regex_pattern, txt)
print(matches) # ['12', '2020']

# PERIOD .

regex_pattern = r"[a]." # this square bracket means any word that starts with a and followed by any character
txt = "Apple and banana are fruits."
matches = re.findall(regex_pattern, txt)
print(matches) # ['Ap', 'an', 'an', 'ar', 'ar']

regex_pattern = r"[a].+" # + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches) # [' and banana are fruits.']

# Zero or more times *

regex_pattern = r"[a].*" # * means zero or more times
txt = "Apple and banana are fruits."
matches = re.findall(regex_pattern, txt)
print(matches) # ['and banana are fruits.']

# Zero or one time ?

txt = """I am not sure if there is a convention how to write the word e-mail.
Some people write it email others may write it E-mail or Email."""
regex_pattern = r"[Ee]-?mail" # ? mdeans zero or one time
matches = re.findall(regex_pattern, txt)
print(matches) # ['e-mail', 'email', 'E-mail', 'Email']

# Quantifier in RegEx

txt = "This regular expression example was made in January 12, 2020."
regex_patter = r"\d{4}" # {4} means exactly four times
matches = re.findall(regex_patter, txt)
print(matches) # ['2020']

regex_patter = r"\d{1,4}" # {1,4} means between one and four times
matches = re.findall(regex_patter, txt)
print(matches) # ['12', '2020']

#Cart ^

txt = "This regular expression example was made in September 30, 2020."
regex_pattern = r"[^A-Za-z ]+" # ^ in set charcater means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches) # ['30,', '2020.']

