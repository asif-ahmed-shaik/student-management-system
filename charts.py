import matplotlib.pyplot as plt

from database import get_students_by_department

def show_department_chart():
    departments = get_students_by_department()

    if not departments:
        print("\nNo data available.")
        input("\nPress Enter to continue...")
        return

    labels = []
    sizes = []

    for department, count in departments:
        labels.append(department)
        sizes.append(count)

        plt.figure(figsize = (6,6))

        plt.pie(
            sizes,
            labels = labels,
            autopct = "%1.1f%%",
            startangle = 90
        )

        plt.title("Students by Department")

        plt.show()