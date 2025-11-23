# Max Jankowski
# csd-325 module 8 assignment
# Bellevue University

import json # imports json library to read and write .json files
            # 'from os import path' not needed as json file is in the same folder

def print_students(students): # defining the function to print out dictionaries containing student info
    for student in students: #looping through each dictionary on the list
        # providing the format of printed info
        print(
            f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")


def main(): #defining the main function
    filename = 'student.json' # providing the file name in the folder to same as variable filename

    with open(filename, 'r') as file: #opening the file in read mode
        students = json.load(file) # opening the file and converting to a list

    print("ORIGINAL STUDENT LIST") # informing user that this is the original list
    print()
    print_students(students) #calling the print_students function
    print()

# Creating the new student dictionary and saving as variable new_student with my info
    new_student = {
        "F_Name": "Max",
        "L_Name": "Jankowski",
        "Student_ID": 12345,
        "Email": "mkjankowski@my365.bellevue.edu"
    }

    students.append(new_student) # adding a new student to the end of students list

    print("UPDATED STUDENT LIST")
    print() # blank lines for formating
    print_students(students) #calls the print student list again with updated info
    print()

    with open(filename, 'w') as file: #opens json file in write mode
        json.dump(students, file, indent=4) # converts python formating to json and writes to file
                                            # indent is for readability of the json file
# notification that file has been updated
    print("The student.json file has been updated!")


if __name__ == '__main__':
    main()