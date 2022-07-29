phone_balance = 10
bank_balance = 50

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
else:
    print('No call made!')

print(phone_balance, bank_balance)
