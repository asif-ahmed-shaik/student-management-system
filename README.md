# Student Management System

A console-based student records system built in Python, developed as a practice project in CRUD operations, data persistence, and object-oriented programming.

## Features

- Add, view, update, and delete student records
- Data persistence via JSON storage (`students.json`)
- Input validation to prevent bad data entry
- In progress: OOP refactor and a Tkinter-based GUI

## Tech Stack

- Python 3
- JSON for data storage
- Tkinter (GUI, in progress)

## Project Structure

```
student-management-system/
├── main.py                 # Entry point — run this to start the program
├── student_operations.py   # Core CRUD logic
├── students.json           # Stored student records
└── data/                   # Supporting data files
```

## How to Run

```bash
git clone https://github.com/asif-ahmed-shaik/student-management-system.git
cd student-management-system
python main.py
```

Requires Python 3.

## What I Learned

Building this project helped me practice:
- File-based data persistence with JSON
- Structuring a multi-file Python program
- Input validation and error handling
- (Ongoing) applying OOP principles to refactor a procedural codebase

## Roadmap

- [ ] Refactor into OOP classes
- [ ] Add a Tkinter GUI
- [ ] Add unit tests
