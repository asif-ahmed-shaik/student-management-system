student = []

print("=" * 45)
print("     STUDENT MANAGEMENT SYSTEM")
print("=" * 45)

print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Exit")

choice = input("\nEnter your choice: ")

print(f"\nYou selected option {choice}")

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

    print(f"\nYou selected option {choice}")

    if choice == "1":
        add_student()
    else:
        print("This option is not implemented yet.")