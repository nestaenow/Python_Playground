# f = open('file_one.txt', 'w')
# f.write("Here's my first file handled in Python! Yay!")
# f.close

# Now let's read the file we created above
# file_one = open('file_one.txt', 'r')
# file_data = file_one.read()
# print(file_data)
# file_one.close

# files = []
# for i in range(10000):
#     files.append(open('file_one.txt', 'r'))
#     print(i)

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open(filename) as actor_name:
        #use the for loop syntax to process each line
        for line in actor_name:
            #and add the actor name to cast_list
            cast_list.append(line.split(',')[0])

    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
print(cast_list)
for actor in cast_list:
    print(actor)
