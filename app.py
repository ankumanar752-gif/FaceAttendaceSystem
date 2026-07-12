from flask import Flask, render_template, request, redirect, session
import sqlite3
import subprocess
import sys
import os
from datetime import datetime
from openpyxl import Workbook
from flask import send_file
import shutil

app = Flask(__name__)
app.secret_key = "faceattendance123"
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "Ankita" and password == "Ankita123":

            session["login"] = True

            return redirect("/")

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")


# ---------------- HOME ----------------
from datetime import datetime

@app.route("/")
def home():

    if "login" not in session:
        return redirect("/login")

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # Total Students
    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    # Today's Attendance
    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        "SELECT COUNT(*) FROM attendance WHERE date=?",
        (today,)
    )

    today_attendance = cursor.fetchone()[0]

    # Students per Department
    cursor.execute("""
        SELECT department, COUNT(*)
        FROM students
        GROUP BY department
    """)

    department_data = cursor.fetchall()

    departments = []
    department_counts = []

    for row in department_data:
        departments.append(row[0])
        department_counts.append(row[1])

    # Recent Attendance
    cursor.execute("""
        SELECT name,time
        FROM attendance
        ORDER BY date DESC,time DESC
        LIMIT 5
    """)

    recent = cursor.fetchall()
    
    # Weekly Attendance
    cursor.execute("""
    SELECT date, COUNT(*)
    FROM attendance
    GROUP BY date
    ORDER BY date DESC
    LIMIT 7
    """)

    weekly = cursor.fetchall()

    weekly.reverse()

    week_labels = []
    week_counts = []

    for row in weekly:

     week_labels.append(row[0])

     week_counts.append(row[1])

    conn.close()
    return render_template(
         "dashboard.html",
        total_students=total_students,
        today_attendance=today_attendance,
        today=today,
        departments=departments,
        department_counts=department_counts,
        recent=recent,
        week_labels=week_labels,
        week_counts=week_counts
    )

# ---------------- ADD STUDENT ----------------
@app.route("/add_student")
def add_student():
    return render_template("add_student.html")


# ---------------- SAVE STUDENT ----------------
@app.route("/save_student", methods=["POST"])
def save_student():

    student_id = request.form["student_id"]
    student_name = request.form["student_name"]
    department = request.form["department"]
    semester = request.form["semester"]

    conn = sqlite3.connect("attendance.db",timeout=10)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        semester TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO students(id,name,department,semester) VALUES(?,?,?,?)",
        (student_id, student_name, department, semester)
    )

    conn.commit()
    conn.close()

    return redirect("/students")


# ---------------- VIEW STUDENTS ----------------
@app.route("/students")
def students():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    conn.close()

    return render_template("students.html", students=data)

# ---------------- CAPTURE FACE ----------------
@app.route("/capture/<int:student_id>")
def capture(student_id):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM students WHERE id=?", (student_id,))
    result = cursor.fetchone()

    conn.close()

    if result is None:
        return "Student not found!"

    student_name = result[0]

    subprocess.Popen([
        sys.executable,
        os.path.join(os.path.dirname(__file__), "capture.py"),
        str(student_id),
        student_name
    ])

    return redirect("/students")


# ---------------- TRAIN MODEL ----------------
@app.route("/train")
def train():

    return render_template("loading.html")

@app.route("/start_training")
def start_training():

    subprocess.run([sys.executable, "train.py"])

    return redirect("/?success=train")


# ---------------- TAKE ATTENDANCE ----------------
@app.route("/attendance")
def attendance():

    subprocess.Popen([sys.executable, "recognize.py"])

    return redirect("/")

@app.route("/reports")
def reports():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id,name,date,time
        FROM attendance
        ORDER BY date DESC,time DESC
    """)

    attendance = cursor.fetchall()

    conn.close()

    return render_template(
        "reports.html",
        attendance=attendance
    )

@app.route("/export")
def export():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name, date, time
        FROM attendance
        ORDER BY date DESC, time DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    wb = Workbook()
    ws = wb.active
    ws.title = "Attendance"

    # Header
    ws.append(["Student ID", "Name", "Date", "Time"])

    # Data
    for row in rows:
        ws.append(row)

    filename = "Attendance_Report.xlsx"
    wb.save(filename)

    return send_file(
        filename,
        as_attachment=True
    )
@app.route("/delete_student/<int:student_id>")
def delete_student(student_id):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # Get student name
    cursor.execute(
        "SELECT name FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:

        student_name = student[0]

        # Delete from students table
        cursor.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )

        # Delete attendance records
        cursor.execute(
            "DELETE FROM attendance WHERE student_id=?",
            (student_id,)
        )

        conn.commit()

        # Delete dataset folder
        folder = f"dataset/{student_name}_{student_id}"

        if os.path.exists(folder):
            shutil.rmtree(folder)

    conn.close()

    return redirect("/students") 
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")   
if __name__ == "__main__":
    app.run(debug=True)