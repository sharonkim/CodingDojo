students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# def nameList(students):
#     for dictionary in students:
#         print "\n"
#         for key in dictionary:
#             print dictionary[key], "",
#
#
# nameList(students)

for student in students:
    print student['first_name'], student['last_name']
