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

print(elements["helium"])  # get and print the helium dictionary
print(elements["hydrogen"]["weight"])  # get and print hydrogen's weight
