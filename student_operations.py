
students = []

import json


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department
    }

    print("Before append:", students)

    students.append(student)

    print("After append:", students)

    save_students()

    print("\nStudent added successfully!")

def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")

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

