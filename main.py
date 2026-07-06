students = []

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

            print("\nStudent Found!")
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


while True:

    print("\n" + "=" * 45)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "6":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("\n⚠️ This feature is coming soon.")