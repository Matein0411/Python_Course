from random import random, randint
import string
import random

# Exercises: Level 1

# Writ a function which generates a six digit/character random_user_id.

def random_user_id():
    user_id = ""
    characters = string.ascii_letters + string.digits
    for _ in range(6):
        user_id += (characters[randint(0, len(characters) - 1)])
    return user_id

print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits
    user_ids = []
    user_id = ""

    num = input("Enter two numbers: like 1, 2: ")
    num1, num2 = num.split(",")

    for _ in range(0, int(num1)):

        for __ in range(0, int(num2)):
            user_id += (characters[randint(0, len(characters) -1)])
        else:
            user_ids.append(user_id)
            user_id = ""
    print(user_ids)


# user_id_gen_by_user()


# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form

def rgb_color_gen():
    rgb = tuple()

    rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
    print(rgb)

rgb_color_gen()

# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
#  0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_color():
    hexa_options = string.digits[:10] + string.ascii_letters[:6]

    hexa_num = "#"

    for _ in range(6):
        hexa_num += hexa_options[randint(0, len(hexa_options) -1)]

    print(hexa_num)


list_of_hexa_color()

# Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_random_colors():
    option = randint(1, 2)
    quantity = randint(1, 10)
    hexa_colors = []
    rgb_colors = []


    hexa_options = string.digits[:10] + string.ascii_letters[:6]

    if(option == 1):
        hexa_num = "#"
        for _ in range(quantity):
            for __ in range(6): 
                hexa_num += hexa_options[randint(0, len(hexa_options) -1)]
            hexa_colors.append(hexa_num)
            hexa_num = "#"
        print(f"{quantity} hexa: {hexa_colors}")

    if(option ==2):
        rgb = tuple()
        for _ in range(quantity):
            rgb = (randint(0, 255),  randint(0, 255), randint(0, 255))
            rgb_colors.append(rgb)
            rgb = tuple()
        print(f"{quantity} rgb: {rgb_colors}")
    
generate_random_colors()

# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffled_list(lst: list):
    random.shuffle(lst)
    print(lst)

lst = [4, 2, 3]

shuffled_list(lst)

# Write a function which returns an array of seven random 
# numbers in a range of 0-9. All the numbers must be unique.

def seven_numbers():
    numbers = set()
    i = 1
    while i <= 7: 
        num = randint(0, 9)
        if num in numbers: # obvio nope, because is a set :)
            i -= 1
        numbers.add(num)
        i += 1
    print(numbers)

seven_numbers()