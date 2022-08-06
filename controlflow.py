phone_balance = 10
bank_balance = 50

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
else:
    print('No call made!')

print(phone_balance, bank_balance)

# if, elif and else statements
season = 'summer'

if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')


# Test 1
#First Example - try changing the value of phone_balance
phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

#Second Example - try changing the value of number

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
age = 35

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(
    age, ticket_price)
print(message)


# Test 2
# '''
# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.
# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 10
guess = 30

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"

print(result)

# Test 3
errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")

# Test 4
points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)

# Loops
list_of_numbers = list(range(1, 10, 2))
print(list_of_numbers)

for number in list_of_numbers:
    print(number)

# Test I
# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

# Test II
sentence = ["the", "quick", "brown", "fox",
            "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line
for word in sentence:
    print(word)

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for i in range(5, 31, 5):
    print(i)

# Test III
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    username = name.replace(' ', '_')
    usernames.append(username.lower())

print(usernames)

# Test IV
usernames = ["Joey Tribbiani", "Monica Geller",
             "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(' ', '_')
print(usernames)

# Test V
tokens = ['<greeting>', '<Hello World!>', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

# Test VI
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += '<li>{}</li>\n'.format(item)
html_str += '</ul>'
print(html_str)

# Test  VII 
# The code below produces an empty array
print(list(range(0,-5)))

# Test VIII
# Using a for loop to create a set of counters
book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes',
              'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)

# Test IX
# Using the get method to create a set of counters
book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes',
              'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin', 'the', "queen's", 'gambit']
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
print(word_counter)

# Test X
# Iterating Through Dictionaries with For Loops
cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

print("Iterating through keys:\n")
for key in cast:
    print(key + '\n')

print("\nIterating through keys and values:\n")
for key, value in cast.items():
    print("{} : {}\n".format(key, value))

# Test XI
# Fruit Basket - Task 1
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for key in basket_items:
    # if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        # This gets the value of the key and adds it to result
        result += basket_items[key]
print(result)

# Test XII
# Counting bot fruits and non-fruits
fruit_count, not_fruit_count = 0, 0

#Iterate through the dictionary
for key in basket_items:
    #if the key is in the list of fruits, add to fruit_count.
    if key in fruits:
        fruit_count += basket_items[key]
#if the key is not in the list, then add to the not_fruit_count
    elif key not in fruits: # A simple else statement will suffice here rather than an elif
        not_fruit_count += basket_items[key] # Instead of using basket_items[key] you can use the items method right from the for loop to access both the keys and values in the dictionary

print(fruit_count, not_fruit_count)


# WHILE Loops
# Test I
# Factorial of a number
number = 6
product = 1
current = 1

while current <= number:
    product *= current
    current += 1
# Factorial of a number with for loop
# for num in range(2, number + 1):
# The start variable starts at 2 here just to make the code succinct since any number times 1 is the number
#    product *= num
print(product)

# Test II
# Count By
start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

# Count By Check
start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)

# Nearest Square
limit = 20

num = 0
squares = []
while (num+1)**2 < limit:
    num += 1
    squares.append(num**2)
nearest_square = num**2

print(nearest_square)
print(squares)

# Test III
# Sum of odd numbers
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
sum_of_odds = 0

for num in range(5):
    if num_list[num] % 2 != 0:
        sum_of_odds += num_list[num]
print(sum_of_odds)
