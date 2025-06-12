#!/usr/bin/python3
import sys
import os

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

# Remove existing file for clean test
if os.path.exists(path):
    os.remove(path)

# Original student
student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

# Save to file
save_to_json_file(j_student_1, path)
print("\nSaved to disk:")
read_file(path)

# New student with fake data
print("\nFake student:")
new_student_1 = Student("Fake", "Fake", 89)
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

# Load JSON and update the new student
new_j_student_1 = load_from_json_file(path)
new_student_1.reload_from_json(new_j_student_1)

print("\nReloaded student:")
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
