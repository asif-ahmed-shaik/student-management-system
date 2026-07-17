
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
        input("\nPress Enter to continue...")
        return

    print("-" * 50)
    print(f"{'ID':<10}{'Name':<20}{'Age':<8}{'Department':<15}")
    print("-" * 50)

    for student in students:
        print(f"{student['id']:<10}{student['name']:<20}{student['age']:<8}{student['department']:<15}")

    print("-" * 50)
    print(f"Total Students: {len(students)}")

    input("\nPress Enter to continue...")


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

        input("\nPress Enter to continue...")


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
            input("\nPress Enter to continue...")
            return

    print("\n Student not found.")

def delete_student():

    print("\n--- Delete Student ---")

    search_id = input("Enter Student ID to delete: ")

    for student in students:

        if student["id"] == search_id:

            print("\nStudent Found!")
            print("----------------------------")
            print(f"ID         : {student['id']}")
            print(f"Name       : {student['name']}")
            print(f"Age        : {student['age']}")
            print(f"Department : {student['department']}")
            print("----------------------------")

            choice = input("Are you sure you want to delete this student? (y/n): ").strip().lower()

            if choice == "y":
                students.remove(student)
                save_students()
                print("\nStudent deleted successfully!")
                input("\nPress Enter to continue...")
            else:
                print("\nDeletion cancelled.")

            return

    print("\nStudent not found.")

