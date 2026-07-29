from database import get_oldest_age, get_total_students, get_average_age, get_youngest_age, get_students_by_department, get_largest_department

def analytics_menu():

    """Displays the analytics menu and handles user input."""

    while True:

        print("\n" + "=" * 45)
        print("      ANALYTICS DASHBOARD")
        print("=" * 45)

        print("1. Total students")
        print("2. Average Age")
        print("3. Youngest Student")
        print("4. Oldest Student")
        print("5. Students by Department")
        print("6. Largest Department")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            total = get_total_students()
            print(f"\nTotal number of students: {total}")
            input("\nPress Enter to continue...")

        elif choice == "2":
            avg = get_average_age()
            print(f"\nAverage age of students: {avg:.2f}")
            input("\nPress Enter to continue...")

        elif choice == "3":
            youngest = get_youngest_age()

            if youngest is None:
                print("\nNo students found.")
            else:
                print(f"\nYoungest Student Age: {youngest} years")

            input("\nPress Enter to continue...")

        elif choice == "4":
            oldest = get_oldest_age()

            if oldest is None:
                print("\nNo students found.")
            else:
                print(f"\nOldest Student Age: {oldest} years")

            input("\nPress Enter to continue...")

        elif choice == "5":
            department = get_students_by_department()

            if not department:
                print("Not students found.")

            else:
                print("Students by department.")
                print("-" * 30)

                for department, count in department:
                    print(f"{department: <15}{count}")

            input("\nPress enter to continue...")

        elif choice == "6":
            largest = get_largest_department()

            if largest is None:
                print("\nNo students found.")
            else:
                department, count = largest

                print("\nLargest Department")
                print("-" * 25)
                print(f"Department : {department}")
                print(f"Students   : {count}")

            input("\nPress enter to continue...")          

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")



