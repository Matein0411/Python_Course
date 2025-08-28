from countries_data import countries_data

# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.

for number in range(11):
    print(number)

# Iterate 10 to 0 using for loop, do the same using while loop.

for number in range(10, -1, -1):
    print(number)

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

for i in range(8):
    print("#"*i)

# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

for i in range(9):
    for j in range (8):
        print("#", end = " ") 
    print() # new line

# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(11):
    for j in range(11):
        print(f"{i} x {j} = {i * j}")
        

# Exercises: Level 2

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
total = 0

for number in range(0, 101): # -> end one before the objetive number
    total += number
else:
    print(total)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

sum_evens: int = 0
sum_odds: float = 0

for number in range(0, 101):
    if(number % 2 == 0):
        sum_evens += number
    else:
        sum_odds += number
else:
    print(f"Sum of evens: {sum_evens}\nSum of odds: {sum_odds}")    


# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

countries_with_land = []
    
for country in countries:
    if "land" in country:
        countries_with_land.append(country)

print (countries_with_land)


# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon'] 
reversed_fruits = []

for i in range(len(fruits) -1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data

unique_languages = set()

for country in countries_data:
    for language in country["languages"]:
        unique_languages.add(language)

print(f"Total of languages: {len(unique_languages)}")

# Find the ten most spoken languages from the data

languages_count = {}

for country in countries_data:
    for language in country["languages"]:
        if language in languages_count:
            languages_count[language] += 1
        else:
            languages_count[language] = 1

language_list = list(languages_count.items())

for i in range(len(language_list)):
    for j in range(i+1, len(language_list)):
        if language_list[j][1] < language_list[i][1]:
            tmp = language_list[i]
            language_list[i] = language_list[j]
            language_list[j] = tmp

print(language_list[::-1][:10])

# Find the 10 most populated countries in the world

countries_pop = {}

for country in countries_data:
    countries_pop[country["name"]] = country["population"]

population_list = list(countries_pop.items())

for i in range(len(population_list)):
    for j in range((i+1), len(population_list)):
        if population_list[i][1] < population_list[j][1]:
            temp = population_list[j] 
            population_list[j] = population_list[i]
            population_list[i] = temp

print(population_list[:10])