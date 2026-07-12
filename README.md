# 🎓 Face Recognition Based Attendance Management System

A modern AI-powered attendance management system that automatically records student attendance using **Face Recognition**. The system is developed using **Python, Flask, OpenCV, SQLite3, HTML, CSS, Bootstrap, and JavaScript**.

---

## 📌 Project Overview

The Face Recognition Based Attendance Management System is designed to automate the attendance process by recognizing students' faces through a webcam. Instead of manually marking attendance, the system identifies registered students and records their attendance in a database.

This project provides a professional web dashboard for administrators to manage students, capture face images, train the recognition model, take attendance, view reports, and export attendance records to Excel.

---

## ✨ Features

- 🔐 Admin Login Authentication
- 👨‍🎓 Add New Students
- 📷 Capture Student Face Images
- 🧠 Train Face Recognition Model (LBPH)
- 🎥 Automatic Face Recognition
- ✅ Mark Attendance Automatically
- 📊 Professional Dashboard
- 📈 Weekly Attendance Chart
- 🥧 Department-wise Student Statistics
- 📋 Attendance Reports
- 📥 Export Attendance to Excel
- 🗑 Delete Students and Associated Data
- 📱 Responsive Bootstrap UI

---

## 🛠 Technologies Used

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js
- Font Awesome

### Backend

- Python
- Flask

### Database

- SQLite3

### Computer Vision

- OpenCV
- LBPH Face Recognizer

### Python Libraries

- Flask
- OpenCV
- NumPy
- Pillow (PIL)
- OpenPyXL
- SQLite3
- OS
- Datetime
- Shutil
- Subprocess

---

## 📂 Project Structure

```
FaceAttendanceSystem/
│
├── app.py
├── capture.py
├── train.py
├── recognize.py
├── attendance.db
├── trainer.yml
├── requirements.txt
│
├── dataset/
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── add_student.html
│   ├── students.html
│   ├── reports.html
│   └── loading.html
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/FaceAttendanceSystem.git
```

Open the project folder

```bash
cd FaceAttendanceSystem
```

---

## Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🔑 Default Login

Username

```
Ankita
```

Password

```
Ankita123
```

> Change these credentials in `app.py` before deploying to production.

---

## 🚀 Working Process

```
Admin Login
      │
      ▼
Add Student
      │
      ▼
Capture Face Images
      │
      ▼
Train LBPH Model
      │
      ▼
Open Webcam
      │
      ▼
Recognize Face
      │
      ▼
Mark Attendance
      │
      ▼
Store in SQLite Database
      │
      ▼
View Reports / Export to Excel
```

---

## 🗄 Database

### Students Table

| Field | Description |
|-------|-------------|
| id | Student ID |
| name | Student Name |
| department | Department |
| semester | Semester |

---

### Attendance Table

| Field | Description |
|-------|-------------|
| student_id | Student ID |
| name | Student Name |
| date | Attendance Date |
| time | Attendance Time |

---

## 📸 Modules

### Login

Secure administrator authentication.

### Dashboard

- Total Students
- Today's Attendance
- Weekly Attendance Graph
- Department-wise Pie Chart
- Recent Attendance

### Student Management

- Add Student
- View Students
- Delete Students

### Face Capture

Captures multiple images for each student.

### Model Training

Trains the LBPH Face Recognition model.

### Attendance

Recognizes faces and records attendance automatically.

### Reports

Displays attendance history.

### Export

Exports attendance records to Excel.

---

## 🧠 Face Recognition Algorithm

This project uses the **Local Binary Pattern Histogram (LBPH)** algorithm provided by OpenCV.

Workflow:

1. Detect face using OpenCV.
2. Extract LBPH facial features.
3. Compare with trained model.
4. Recognize student.
5. Mark attendance if not already recorded for the day.

---

## 📊 Future Enhancements

- Cloud Database (MySQL/PostgreSQL)
- Mobile Application
- Deep Learning Face Recognition (FaceNet/InsightFace)
- Email Notifications
- QR Code Integration
- Student Login Portal
- Attendance Analytics
- Multi-Camera Support

---

## ✅ Advantages

- Fully Automated Attendance
- Eliminates Proxy Attendance
- Saves Time
- Improves Accuracy
- Easy to Use
- Lightweight Database
- Excel Report Generation

---

## ⚠ Limitations

- Requires Good Lighting
- Webcam Required
- Local Deployment by Default
- Retraining Required After Adding New Students

---

## 👩‍💻 Developed By

**Ankita**

B.Tech Computer Science Engineering

Yadavindra Department of Engineering

Punjabi University

---

## 📚 References

- https://opencv.org/
- https://flask.palletsprojects.com/
- https://docs.python.org/
- https://www.sqlite.org/
- https://getbootstrap.com/
- https://www.chartjs.org/

---

## ⭐ Acknowledgement

This project was developed as a Final Year Major Project to demonstrate the practical implementation of Artificial Intelligence, Computer Vision, and Web Development technologies for automating student attendance using facial recognition.

---

### ⭐ If you found this project useful, don't forget to star the repository on GitHub!trtrrrrrrr 