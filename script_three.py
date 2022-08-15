names =  input('Enter the names separated by commas: ').title().split(",")# get and process input for a list of names
# get and process input for a list of the number of assignments
assignments = input('Enter the assignment counts separated by commas: ').title().split(",")
# get and process input for a list of grades
grades = input('Enter the grades separated by commas: ').title().split(",") 

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2 ))