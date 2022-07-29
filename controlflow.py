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
