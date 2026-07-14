
students = []

import json

def get_valid_student_id():
    while True:
        student_id = input("Enter Student ID: ").strip()

        if student_id == "":
            print("Student ID cannot be empty.")

        elif any(student["id"] == student_id for student in students):
            print("Student ID already exists. Please enter a different ID.")

        else:
            return student_id

def get_valid_age():
    while True:
        age = input("Enter Age: ").strip()

        if age == "":
            print("Age cannot be empty.")

        elif not age.isdigit():
            print("Age must contain only numbers.")

        elif int(age) < 16 or int(age) > 100:
            print("Age must be between 16 and 100.")

        else:
            return age

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("This field cannot be empty.")
        else:
            return value

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def load_students():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []


def add_student():
    print("\n--- Add Student ---")

    student_id = get_valid_student_id()

    name = get_non_empty_input("Enter Student Name: ")

    age = get_valid_age()

    department = get_non_empty_input("Enter Department: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department
    }

    students.append(student)

    save_students()

    print("\n Student added successfully!")


def view_students():

    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("----------------------------")
        print(f"ID         : {student['id']}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Department : {student['department']}")
    print("----------------------------")


def search_student():

    print("\n--- Search Student ---")

    search_id = input("Enter Student ID: ")

    found = False

    for student in students:

        if student["id"] == search_id:

            print("\n Student Found!")
            print("----------------------------")
            print(f"ID         : {student['id']}")
            print(f"Name       : {student['name']}")
            print(f"Age        : {student['age']}")
            print(f"Department : {student['department']}")
            print("----------------------------")

            found = True
            break

    if not found:
        print("\n Student not found.")


def update_student():

    print("\n--- Update Student ---")

    search_id = input("Enter Student ID to update: ")

    for student in students:

        if student["id"] == search_id:

            print("\nStudent Found!")

            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["department"] = input("Enter new department: ")

            save_students()

            print("\n Student updated successfully!")
            return

    print("\n Student not found.")

def delete_student():

    print("\n--- Delete Student ---")

    search_id = input("Enter Student ID to delete: ")

    for student in students:

        if student["id"] == search_id:

            students.remove(student)

            save_students()

            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")

