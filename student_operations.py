import json
import os
from student import Student

students = []

# -----------------------------
# Helper Functions
# -----------------------------

def get_valid_student_id():
    while True:
        student_id = input("Enter Student ID: ").strip()

        if student_id == "":
            print("Student ID cannot be empty.")

        elif any(student.id == student_id for student in students):
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
    try:
        student_data = []
        for student in students:
            student_data.append(student.to_dict())

        with open("students.json", "w") as file:
            json.dump(student_data, file, indent=4)

    except Exception as e:
        print(f"\nError saving students: {e}")


def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            student_data = json.load(file)

        students = []

        for data in student_data:
            students.append(Student.from_dict(data))

    except FileNotFoundError:
        students = []
        print("students.json not found. Starting with an empty database.")

    except json.JSONDecodeError:
        students = []
        print("students.json is corrupted. Starting with an empty database.")

# -----------------------------
# Student Operations
# -----------------------------

def add_student():
    print("\n--- Add Student ---")

    student_id = get_valid_student_id()
    name = get_non_empty_input("Enter Student Name: ")
    age = get_valid_age()
    department = get_non_empty_input("Enter Department: ")

    student = Student(
        student_id,
        name,
        age,
        department
    )

    students.append(student)
    save_students()

    print("\nStudent added successfully.")
    input("\nPress Enter to continue...")


def view_students():
    print("\n--- Student Records ---")

    if not students:
        print("No students found.")
        input("\nPress Enter to continue...")
        return

    print("-" * 55)
    print(f"{'ID':<10}{'Name':<20}{'Age':<8}{'Department':<15}")
    print("-" * 55)

    for student in students:
        print(
            f"{student.id:<10}"
            f"{student.name:<20}"
            f"{student.age:<8}"
            f"{student.department:<15}"
        )

    print("-" * 55)
    print(f"Total Students: {len(students)}")

    input("\nPress Enter to continue...")


def search_student():
    print("\n--- Search Student ---")

    search_id = input("Enter Student ID: ").strip()

    found = False

    for student in students:

        if student.id == search_id:

            print("\nStudent Found!")
            print(student)
            print("----------------------------")

            found = True
            break

    if not found:
        print("\nStudent not found.")

    input("\nPress Enter to continue...")


def update_student():
    print("\n--- Update Student ---")

    search_id = input("Enter Student ID to update: ").strip()

    for student in students:

        if student.id == search_id:

            print("\nStudent Found!")

            student.name = get_non_empty_input("Enter new name: ")
            student.age = get_valid_age()
            student.department = get_non_empty_input("Enter new department: ")

            save_students()

            print("\nStudent updated successfully.")
            input("\nPress Enter to continue...")
            return

    print("\nStudent not found.")
    input("\nPress Enter to continue...")


def delete_student():
    print("\n--- Delete Student ---")

    search_id = input("Enter Student ID to delete: ").strip()

    for student in students:

        if student.id == search_id:

            print(student)

            choice = input(
                "Are you sure you want to delete this student? (y/n): "
            ).strip().lower()

            if choice == "y":
                students.remove(student)
                save_students()
                print("\nStudent deleted successfully.")
            else:
                print("\nDeletion cancelled.")

            input("\nPress Enter to continue...")
            return

    print("\nStudent not found.")
    input("\nPress Enter to continue...")

