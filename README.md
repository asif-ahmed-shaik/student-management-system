# Student Management System (Python + SQLite)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

A console-based **Student Management System** built with **Python** and **SQLite**, featuring CRUD operations, object-oriented programming, SQL-powered analytics, and data visualization using **Matplotlib**.

This project was developed alongside my **B.Tech Computer Science Engineering** coursework as a way to apply classroom concepts through hands-on software development while continuously improving a single application as I learned new technologies.

---

# About the Project

The Student Management System is a menu-driven console application that allows users to efficiently manage student records.

Rather than building several unrelated practice programs, I chose to continuously improve this project as I learned new concepts. It started as a simple CRUD application using Python lists, later evolved to JSON-based storage, and was eventually migrated to **SQLite** for persistent database management.

As the project grew, I added an **Analytics Dashboard** powered by SQL aggregate queries and interactive data visualizations using Matplotlib. Along the way, the application was refactored into a modular, multi-file architecture following better software engineering practices.

This project helped me strengthen my understanding of:

- Python Programming
- Object-Oriented Programming (OOP)
- SQLite Database Integration
- SQL (CRUD & Aggregate Queries)
- Data Analytics Fundamentals
- Data Visualization with Matplotlib
- Debugging & Refactoring
- Git & GitHub Workflow

---

# Features

## Student Management

- Add new student records
- View all students
- Search students by Student ID
- Update student information
- Delete student records with confirmation
- Duplicate Student ID prevention
- Input validation for IDs, names, age, and department

---

## Database

- SQLite database (`students.db`)
- Automatic database creation
- Automatic table creation
- Persistent storage
- Dedicated database access layer
- Parameterized SQL queries (SQL Injection safe)

---

## Analytics Dashboard

- Total number of students
- Average student age
- Youngest student
- Oldest student
- Students grouped by department
- Largest department

---

## Data Visualization

- Department Distribution Pie Chart
- Age Distribution Bar Chart

Charts are generated dynamically using live data stored inside the SQLite database.

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core application development |
| SQLite3 | Relational database |
| SQL | CRUD operations & analytics |
| Matplotlib | Data visualization |
| Git | Version control |
| GitHub | Source code hosting |

---

# Repository Structure

```text
student-management-system/
│
├── main.py
├── student.py
├── student_operations.py
├── database.py
├── analytics.py
├── charts.py
├── students.db
├── .gitignore
├── README.md
└── LICENSE
```

### Module Responsibilities

| File | Responsibility |
|------|----------------|
| `main.py` | Program entry point and main menu |
| `student.py` | Student model |
| `student_operations.py` | CRUD operations and validation |
| `database.py` | SQLite database layer |
| `analytics.py` | Analytics dashboard |
| `charts.py` | Data visualization |

---

# Application Architecture

```text
                    +----------------+
                    |    main.py     |
                    +-------+--------+
                            |
            +---------------+---------------+
            |                               |
            ▼                               ▼
+-------------------------+      +------------------------+
| student_operations.py   |      |    analytics.py        |
+------------+------------+      +------------+-----------+
             |                                |
             ▼                                ▼
       +------------+               +----------------+
       | database.py|-------------->|   charts.py    |
       +------+-----+               +----------------+
              |
              ▼
      +------------------+
      |   SQLite Database|
      +------------------+
```

The application follows a modular architecture where each file has a clearly defined responsibility, making the project easier to maintain and extend.

---

# Getting Started

## Prerequisites

- Python 3.x

---

## Clone the Repository

```bash
git clone https://github.com/asif-ahmed-shaik/student-management-system.git
```

---

## Navigate to the Project

```bash
cd student-management-system
```

---

## Install Dependencies

```bash
pip install matplotlib
```

---

## Run the Application

```bash
python main.py
```

On the first run, the application automatically creates the SQLite database (`students.db`) along with the required tables.

---

# Application Preview

Application screenshots and a short demonstration GIF will be added in a future update.

The current version includes:

- Console-based Student Management System
- SQLite Database
- Analytics Dashboard
- Department Distribution Pie Chart
- Age Distribution Bar Chart

---

# SQL Concepts Demonstrated

This project applies SQL beyond basic CRUD operations by generating meaningful insights from stored data.

### CRUD Operations

- INSERT
- SELECT
- UPDATE
- DELETE

### Aggregate Functions

- COUNT()
- AVG()
- MIN()
- MAX()

### Query Techniques

- GROUP BY
- ORDER BY
- LIMIT
- Parameterized Queries

---

# Project Evolution

One objective of this repository is to document how the project evolved as I learned new programming concepts and software engineering practices.

| Version | Milestone |
|----------|-----------|
| **v1.0** | Basic CRUD using Python Lists |
| **v2.0** | JSON File Persistence |
| **v2.1** | Input Validation |
| **v2.2** | Code Refactoring & Helper Functions |
| **v3.0** | OOP foundations (`Student` class; `StudentManager` refactor in progress) |
| **v4.0** | SQLite Database Migration |
| **v5.0** | SQL Analytics Dashboard |
| **v5.1** | Matplotlib Data Visualizations |

Each version introduced new concepts while improving the architecture, maintainability, and overall quality of the project.

---

# What I Learned

Developing this project strengthened my understanding of:

- Writing modular Python applications
- Object-Oriented Programming principles
- Database design using SQLite
- SQL CRUD operations
- SQL aggregate functions for analytics
- Migrating applications from JSON storage to relational databases
- Data visualization with Matplotlib
- Debugging serialization, database, SQL, and visualization issues
- Refactoring an existing codebase instead of rewriting it
- Git branching, pull requests, merging, and collaborative workflows

---

# Future Improvements

- StudentManager architecture refinement
- Unit testing using Pytest
- Student GPA management
- Attendance management
- CSV / Excel import and export
- Logging system
- Tkinter desktop GUI
- Flask web version
- Additional analytics and visualizations
- README screenshots and demo GIF

---

# Author

**Asif Ahmed Shaik**

B.Tech Computer Science Engineering Student

Interested in **Data Analytics**, **Data Engineering**, and **Software Development**.

**GitHub**
https://github.com/asif-ahmed-shaik

**LinkedIn**
https://www.linkedin.com/in/asif-shaik-cse/

---

# Why This Project?

This repository represents more than a finished application—it documents my learning journey.

Instead of creating multiple small practice projects, I chose to continuously improve a single application as I learned Python, Object-Oriented Programming, SQL, SQLite, data visualization, and professional Git workflows.

The result is a project that demonstrates not only the final functionality, but also the process of incremental development, debugging, refactoring, and applying new concepts over time.