# f = open('file_one.txt', 'w')
# f.write("Here's my first file handled in Python! Yay!")
# f.close

# Now let's read the file we created above
# file_one = open('file_one.txt', 'r')
# file_data = file_one.read()
# print(file_data)
# file_one.close

files = []
for i in range(10000):
    files.append(open('file_one.txt', 'r'))
    print(i)
