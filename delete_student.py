import sqlite3

student_id = int(input("Enter Student ID to delete: "))

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM students WHERE id=?", (student_id,))

conn.commit()
conn.close()

print("Student deleted successfully!")