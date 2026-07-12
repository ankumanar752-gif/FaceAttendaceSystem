import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    semester TEXT
)
""")

# Attendance table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    name TEXT,
    date TEXT,
    time TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")