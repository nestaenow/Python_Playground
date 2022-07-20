first_word = 'Hello'
second_word = 'There!'

#Using the + operator to concatinate two strings
print (first_word + ' ' + second_word)

#To print a string several times 
print (first_word * 4)

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + ' accessed the site ' + url + ' at ' + timestamp + '.')

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"
#todo: calculate how long this name is
name_length = len(given_name + middle_names + family_name) + 2
#2 accounts for the two spaces between the names

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
total_sales = int(mon_sales)+int(tues_sales) + \
    int(wed_sales)+int(thurs_sales)+int(fri_sales)
total_sales = str(total_sales)
print("This week's total sales: " + total_sales)

# Write two lines of code below, each assigning a value to a variable
names = "john snow"
age = 20

# Now write a print statement using .format() to print out a sentence and the
#   values of both of the variables
print('His name is {} and is {} years old'.format(names.title(), age))


verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don't deal in lies,\nOr being hated, don't give way to hating,\n  And yet don't look too good, nor talk too wise:"

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print("The length of the string variable verse is {}".format(len(verse)))
print("The index of the first occurrence of the word 'and' in the verse is {}".format(
    verse.find('and')))
print("The index of the last occurrence of the word 'you' in the verse is {}".format(
    verse.rfind('you')))
print("The count of occurrences of the word 'you' in the verse is {}".format(
    verse.count('you')))
