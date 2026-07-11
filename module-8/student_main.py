# Eric Sengvanhpheng
# July 2026
# Advanced Python 8.2

import json

# define the function (put file opening and loading inside here)
def loop_json_list(file_path): 

    with open(file_path) as f: # use file path variable here
       data = json.load(f)

    print(type(data)) # get data type from the import, indent stays inside funtion
    print()

    # loop through list
    for student in data:
        print(f"{student['F_Name']}, {student['L_Name']} :ID {student['Student_ID']}, Email = {student['Email']}")

# original list output
print("---- Notification: This is the original student list ----")
loop_json_list('Student.json')
print()

# modify the file
with open('Student.json') as f: # use file path variable here
    class_list = json.load(f)

# create new dictionary to append
my_data = {
    "F_Name": "Eric",
    "L_Name": "Sengvanhpheng",
    "Student_ID": 22084,
    "Email": "erxnoi@gmail.com"
}

# append new dictionary to file
class_list.append(my_data)

# Use json dump() function to append new data
with open('Student.json', 'w') as f:
    json.dump(class_list, f, indent=2)

# Output notification that file updated
print("\n [SUCCESS] The Student.json file has been updated")

# print notification for updated list
print("---- Notification: This is the updated student list ----")
print()

# call function for original and updated list
loop_json_list('Student.json')