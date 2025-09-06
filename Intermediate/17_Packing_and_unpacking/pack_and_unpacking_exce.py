# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a 
# variable nordic_countries, store Estonia and Russia in es, and ru respectively.


names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
nordic_countries = []
es = ""
ru = ""

for i, country in enumerate(names):
    if i < 5:
        nordic_countries.append(country)
    if names[i] == "Estonia":
        es = country
    if names[i] == "Russia":
        ru = country

print(nordic_countries, es, ru)
