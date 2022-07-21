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