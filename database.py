import sqlite3

from student import Student


def create_table():
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    department TEXT NOT NULL
    )
    """)

    connection.commit()

    print("Students table created successfully!")

    connection.close()

def insert_student(student):
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students(id, name, age, department)
        VALUES(?, ?, ?, ?)
    """,(
        student.id,
        student.name,
        int(student.age),
        student.department
        ))

    connection.commit()

    connection.close()

def get_all_students():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM students
    """)

    rows = cursor.fetchall()

    connection.close()

    students = []

    for row in rows:

        students.append(Student.from_row(row))

    return students


def get_student_by_id(student_id):
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM students WHERE id = ?
    """,(student_id,))

    row = cursor.fetchone()

    connection.close()

    if row:
        return Student.from_row(row)

    return None


def update_student_in_db(student):
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, department = ?
        WHERE id = ?
    """, (
        student.name,
        int(student.age),
        student.department,
        student.id
    ))

    connection.commit()

    connection.close()


def delete_student_from_db(student_id):
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM students WHERE id = ?
        """, (student_id,))

    connection.commit()

    connection.close()


def get_total_students():
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) FROM students
        """)

    result = cursor.fetchone()

    connection.close()

    return result[0]

def get_average_age():
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT AVG(age) FROM students
        """)

    result = cursor.fetchone()

    connection.close()

    return result[0]

def get_youngest_age():
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT MIN(age) FROM students
        """)

    result = cursor.fetchone()

    connection.close()

    if result[0] is None:
        return None

    return result[0]


def get_oldest_age():
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT MAX(age) FROM students
        """)

    result = cursor.fetchone()

    connection.close()

    if result[0] is None:
        return None

    return result[0]


def get_students_by_department():
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT department, COUNT(*) FROM students
        GROUP BY department;
        """)

    result = cursor.fetchall()

    connection.close()

    return result


def get_largest_department():
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT department, COUNT(*) AS total_students FROM students
        GROUP BY department
        ORDER BY total_students DESC
        LIMIT 1;
        """)

    result = cursor.fetchone()

    connection.close()

    return result