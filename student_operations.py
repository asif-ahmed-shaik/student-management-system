from student import Student
from database import delete_student_from_db, get_all_students, get_student_by_id, insert_student, update_student_in_db

# -----------------------------
# Helper Functions
# -----------------------------

def get_valid_student_id():
    while True:
        student_id = input("Enter Student ID: ").strip()

        if student_id == "":
            print("Student ID cannot be empty.")

        elif get_student_by_id(student_id):
            print("Student ID already exists.")

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

    #students.append(student)
    #save_students()

    insert_student(student)

    print("\nStudent added successfully.")
    input("\nPress Enter to continue...")


def view_students():
    print("\n--- Student Records ---")

    students = get_all_students()

    if not students:
        print("No students found.")
        input("\nPress Enter to continue...")
        return

    print("-" * 55)
    print(f"{'ID':<10}{'Name':<20}{'Age':<8}{'Department':<15}")
    print("-" * 55)

    for student in students:
        print(f"{student.id:<10}{student.name:<20}{str(student.age):<10}{student.department:<15}")

    print("-" * 55)
    print(f"Total Students: {len(students)}")

    input("\nPress Enter to continue...")


def search_student():
    print("\n--- Search Student ---")

    search_id = input("Enter Student ID: ").strip()

    student = get_student_by_id(search_id)

    if student:
        print(student)
    else:
        print("\nStudent not found.")

    input("\nPress Enter to continue...")


def update_student():
    print("\n--- Update Student ---")

    search_id = input("Enter Student ID to update: ").strip()

    student = get_student_by_id(search_id)

    if student:
        print("\nStudent Found!")

        student.name = get_non_empty_input("Enter new name: ")
        student.age = get_valid_age()
        student.department = get_non_empty_input("Enter new department: ")

        update_student_in_db(student)

        print("\nStudent updated successfully.")
        input("\nPress Enter to continue...")
        return

    print("\nStudent not found.")
    input("\nPress Enter to continue...")


def delete_student():

    print("\n--- Delete Student ---")

    search_id = input("Enter Student ID to delete: ").strip()

    student = get_student_by_id(search_id)

    if student is None:
        print("\nStudent not found.")
        input("\nPress Enter to continue...")
        return

    print(student)

    choice = input("Are you sure you want to delete this student? (y/n): ").strip().lower()

    if choice == "y":
        delete_student_from_db(student.id)
        print("\nStudent deleted successfully.")
    else:
        print("\nDeletion cancelled.")

    input("\nPress Enter to continue...")

