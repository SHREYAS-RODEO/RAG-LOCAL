import sqlite3
import os

DB_DIR = os.path.join(os.path.dirname(__file__), "../data")
os.makedirs(DB_DIR, exist_ok=True)

# ---------- STUDENTS DB ----------
students_db = os.path.join(DB_DIR, "students.db")
with sqlite3.connect(students_db) as conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS students")
    c.execute("""
        CREATE TABLE students (
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            year INTEGER,
            email TEXT
        )
    """)
    c.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", [
        (101, "Alice", "ISE", 3, "alice@nmit.ac.in"),
        (102, "Bob", "CSE", 2, "bob@nmit.ac.in"),
        (103, "Charlie", "ISE", 3, "charlie@nmit.ac.in")
    ])

# ---------- TEACHERS DB ----------
teachers_db = os.path.join(DB_DIR, "teachers.db")
with sqlite3.connect(teachers_db) as conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS teachers")
    c.execute("""
        CREATE TABLE teachers (
            teacher_id INTEGER PRIMARY KEY,
            name TEXT,
            subject TEXT,
            email TEXT
        )
    """)
    c.executemany("INSERT INTO teachers VALUES (?, ?, ?, ?)", [
        (201, "Dr. Smith", "Machine Learning", "smith@nmit.ac.in"),
        (202, "Prof. Jane", "DBMS", "jane@nmit.ac.in")
    ])

# ---------- GRADES DB ----------
grades_db = os.path.join(DB_DIR, "grades.db")
with sqlite3.connect(grades_db) as conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS grades")
    c.execute("""
        CREATE TABLE grades (
            student_id INTEGER,
            subject TEXT,
            score REAL
        )
    """)
    c.executemany("INSERT INTO grades VALUES (?, ?, ?)", [
        (101, "DBMS", 89.5),
        (102, "Machine Learning", 92.0),
        (103, "DBMS", 76.0)
    ])

# ---------- ATTENDANCE DB ----------
attendance_db = os.path.join(DB_DIR, "attendance.db")
with sqlite3.connect(attendance_db) as conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS attendance")
    c.execute("""
        CREATE TABLE attendance (
            student_id INTEGER,
            date TEXT,
            status TEXT
        )
    """)
    c.executemany("INSERT INTO attendance VALUES (?, ?, ?)", [
        (101, "2025-08-01", "Present"),
        (102, "2025-08-01", "Absent"),
        (103, "2025-08-01", "Present")
    ])

print("✅ All databases created successfully in the data/ directory.")
