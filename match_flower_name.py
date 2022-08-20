# Write your code here
flower_dict = {}

def name_and_flower(file_name):
    with open(file_name) as name_flower:
        for line in name_flower:
            flower_dict[line.split(':')[0]] = line.split(':')[1]
# HINT: create a dictionary from flowers.txt
def first_and_last_name():
    name = input('Enter your first and last name: ')
    return name[0]
# HINT: create a function to ask for user's first and last name
name_and_flower('flowers.txt')
fl_name = first_and_last_name()
if fl_name in flower_dict:
    print('Unique flower name with the first letter: {}'.format(flower_dict[fl_name]))
# print the desired output
print(flower_dict)
