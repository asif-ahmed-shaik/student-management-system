from database import get_total_students, get_average_age

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
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            total = get_total_students()
            print(f"\nTotal number of students: {total}")
            print("\nPress Enter to continue...")

        elif choice == "2":
            avg = get_average_age()
            print(f"\nAverage age of students: {avg:.2f}")
            print("\nPress Enter to continue...")

        elif choice == "3":
            print("Coming soon")

        elif choice == "4":
            print("Coming soon")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")



