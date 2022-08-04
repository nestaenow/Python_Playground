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
    name = usernames[index].lower().replace(' ', '_')
    usernames[index] = name

print(usernames)
