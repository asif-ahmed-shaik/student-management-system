import matplotlib.pyplot as plt

from database import get_students_by_department, get_age_distribution

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



def show_age_distribution():

    data = get_age_distribution()

    if not data:
        print("No data available.")
        input("\nPress Enter to continue...")
        return

    ages = []
    counts = []

    for age, count in data:
        ages.append(age)
        counts.append(count)

    plt.figure(figsize=(8,5))

    plt.bar(ages, counts)

    plt.title("Age Distribution")

    plt.xlabel("Age")

    plt.ylabel("Number of Students")

    plt.grid(axis="y")

    plt.show()