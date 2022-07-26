months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

q3 = months[6:9]
# [ 'July', 'August', 'September']
print(q3)  

first_half = months[:6]
# ['January', 'February', 'March', 'April', 'May', 'June']
print(first_half)  

second_half = months[6:]
# ['July', 'August', 'September', 'October', 'November', 'December']
print(second_half)

# Using the membership operators 'in' and 'not in'
print('Sunday' in months, 'Sunday' not in months)

# List Indexing
month = 8
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month - 1]

print(num_days)

# Slicing Lists
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
eclipse_dates = eclipse_dates[-3:]
# This could equally work --> eclipse_dates = eclipse_dates[-3:len(eclipse_dates)
print(eclipse_dates)

# The join method
name = "-".join(["Garcia", "O'Kelly"])
print(name)

# The append method
letters = ['a', 'b', 'c', 'd']
letters.append('e')
print(letters)

# Tuples
location = (13.4125, 103.866667)
# Unpacking a tuple will be like this
longitude, latitude = location

print("Latitude:", location[0])
print("Longitude:", location[1])

# Sets
countries = ['Angola', 'Maldives', 'India', 'United States', 'India', 'Denmark', 'Sweden', 'Ghana']

print(len(countries))
print(countries[:5])
# ['Angola', 'Maldives', 'India', 'United States', 'India']

country_set = set(countries)
print(country_set)

country_set.add('Italy')
country_set.pop()
print(country_set)

# Dictionaries
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

# print the value mapped to "helium"
print(elements["helium"]) 

# insert "lithium" with a value of 3 into the dictionary
elements["lithium"] = 3
print(elements)

# Testing identity operators
n = elements.get("dilithium")
print(n is None)
print(n is not None)

# get with a default value
print(elements.get('kryptonite', 'There\'s no such element!'))


# Compoud Data Structures
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
            "helium": {"number": 2,
                       "weight": 4.002602,
                       "symbol": "He"}}

# create a new oxygen dictionary
oxygen = {"number": 8, "weight": 15.999, "symbol": "O"}
# assign 'oxygen' as a key to the elements dictionary
elements["oxygen"] = oxygen

print('elements = ', elements)
print(elements["helium"])  # get and print the helium dictionary
print(elements["hydrogen"]["weight"])  # get and print hydrogen's weight


#### Retain ####
verse_dict = {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1,
              'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1])
