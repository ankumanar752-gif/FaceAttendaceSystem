# 🎓 Face Recognition Based Attendance Management System

A web-based **Face Recognition Attendance Management System** that automatically identifies registered students through a webcam and records their attendance.

The system combines **Python, Flask, OpenCV, LBPH Face Recognition, SQLite, HTML, CSS, Bootstrap, JavaScript, and Excel reporting** to provide an easy-to-use attendance management solution.

---

## 📌 Project Overview

Manual attendance takes time and can allow proxy attendance. This project automates the process by using **face detection and face recognition**.

An administrator can:

* Add student information
* Capture student face images using a webcam
* Train the face recognition model
* Start automatic face recognition
* Mark attendance automatically
* View attendance reports
* Export attendance records to Excel
* Delete students and their associated attendance data

The project is designed primarily for **local computer/laptop use with a webcam**.

---

## ✨ Features

### 🔐 Admin Login

* Administrator login page
* Session-based authentication

### 👨‍🎓 Student Management

* Add students
* Store student ID, name, department, and semester
* View registered students
* Delete students

### 📷 Face Dataset Collection

* Uses the computer's webcam
* Detects the student's face
* Captures up to 50 face images
* Stores images in a student-specific dataset folder

### 🧠 Face Recognition

* Uses OpenCV's **LBPH Face Recognizer**
* Uses Haar Cascade for face detection
* Recognizes registered students
* Displays the student's name and recognition confidence

### ✅ Automatic Attendance

* Automatically records recognized students
* Stores date and time
* Prevents duplicate attendance for the same student on the same day

### 📊 Dashboard

* Total number of students
* Today's attendance
* Department-wise student statistics
* Weekly attendance statistics
* Recent attendance records

### 📋 Attendance Reports

* View attendance history
* Display student ID, name, date, and time

### 📥 Excel Export

* Export attendance records to an `.xlsx` file
* Uses OpenPyXL for Excel generation

---

## 🛠️ Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Python       | Main programming language      |
| Flask        | Web application framework      |
| OpenCV       | Face detection and recognition |
| LBPH         | Face recognition algorithm     |
| Haar Cascade | Face detection                 |
| NumPy        | Image/data processing          |
| Pillow       | Image processing               |
| SQLite       | Database                       |
| OpenPyXL     | Excel report generation        |
| HTML5        | Web page structure             |
| CSS3         | Styling                        |
| Bootstrap    | Responsive UI                  |
| JavaScript   | Client-side functionality      |
| Chart.js     | Dashboard charts               |

---

## 🧠 How the System Works

The complete workflow is:

```text
              ┌─────────────────┐
              │   Admin Login   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Add Student    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Capture Face    │
              │    Images       │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Train LBPH      │
              │ Recognition     │
              │     Model       │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Start Webcam    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Detect Face     │
              │ Haar Cascade    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Recognize Face  │
              │      LBPH       │
              └────────┬────────┘
                       │
                 Recognized?
                  /         \
                Yes          No
                 │            │
                 ▼            ▼
        ┌──────────────┐   Unknown
        │ Mark         │
        │ Attendance   │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ SQLite       │
        │ Database     │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ Reports /    │
        │ Excel Export │
        └──────────────┘
```

---

## 📂 Project Structure

```text
FaceAttendaceSystem/
│
├── app.py                         # Main Flask application
├── capture.py                     # Captures student face images
├── train.py                       # Trains LBPH face recognition model
├── recognize.py                   # Recognizes faces and marks attendance
├── database.py                    # Creates SQLite database tables
├── delete_student.py              # Deletes student from database
├── attendance.py                  # Attendance-related file
│
├── attendance/
│   └── attendance.csv
│
├── attendance.db                  # SQLite database
│
├── dataset/
│   ├── StudentName_ID/
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   └── ...
│   └── ...
│
├── haarcascade/
│   └── haarcascade_frontalface_default.xml
│
├── trainer/
│   └── trainer.yml                # Trained LBPH model
│
├── static/
│   └── css/
│       ├── dashboard.css
│       ├── login.css
│       ├── style.css
│       └── js/
│           └── script.js
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── add_student.html
│   ├── students.html
│   ├── reports.html
│   └── loading.html
│
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/FaceAttendaceSystem.git
```

Move into the project directory:

```bash
cd FaceAttendaceSystem
```

---

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Important:** This project requires `opencv-contrib-python` because the LBPH face recognizer is provided through OpenCV's `cv2.face` module.

If necessary, install it manually:

```bash
pip install opencv-contrib-python
```

---

## 🗄️ Database Setup

Run:

```bash
python database.py
```

This creates the SQLite database and the required tables.

The project contains two main tables:

### Students

| Column       | Description        |
| ------------ | ------------------ |
| `id`         | Student ID         |
| `name`       | Student name       |
| `department` | Student department |
| `semester`   | Student semester   |

### Attendance

| Column       | Description          |
| ------------ | -------------------- |
| `id`         | Attendance record ID |
| `student_id` | Student ID           |
| `name`       | Student name         |
| `date`       | Attendance date      |
| `time`       | Attendance time      |

---

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 👨‍🎓 Adding a Student

1. Login to the system.
2. Open **Add Student**.
3. Enter:

   * Student ID
   * Student Name
   * Department
   * Semester
4. Save the student.
5. Select the student from the student list.
6. Start face capture.
7. Look at the webcam.
8. The system captures up to **50 face images**.

The images are stored in:

```text
dataset/StudentName_StudentID/
```

---

## 🧠 Training the Face Recognition Model

After capturing face images, the model needs to be trained.

The training process:

1. Reads images from the `dataset` directory.
2. Converts images to grayscale.
3. Extracts the student ID from the dataset folder name.
4. Trains the LBPH face recognizer.
5. Saves the trained model as:

```text
trainer/trainer.yml
```

The application provides a **Train Model** option from the dashboard.

You can also run:

```bash
python train.py
```

---

## 📷 Taking Attendance

After training:

1. Open the attendance section.
2. The webcam starts.
3. Haar Cascade detects faces.
4. LBPH predicts the identity of the detected face.
5. If the face is recognized, the student's name is displayed.
6. The system checks whether attendance has already been recorded for that student on the current date.
7. If not already marked, attendance is inserted into SQLite.

Attendance contains:

```text
Student ID
Student Name
Date
Time
```

Press **ESC** to stop face recognition.

---

## 🔍 Face Detection

The project uses the Haar Cascade classifier:

```text
haarcascade/haarcascade_frontalface_default.xml
```

It detects faces from the webcam video stream before the recognition algorithm attempts to identify them.

---

## 🧠 Face Recognition Algorithm — LBPH

The system uses **Local Binary Pattern Histogram (LBPH)** for face recognition.

Basic process:

```text
Input Image
     ↓
Convert to Grayscale
     ↓
Detect Face
     ↓
Extract Local Binary Patterns
     ↓
Create Histograms
     ↓
Compare With Trained Model
     ↓
Predict Student ID
     ↓
Mark Attendance
```

The recognition code uses a confidence/distance threshold to determine whether a detected face should be treated as a known student.

---

## 📊 Dashboard

The dashboard provides an overview of attendance data.

It includes:

* 👨‍🎓 Total students
* ✅ Today's attendance
* 📈 Weekly attendance
* 🥧 Department-wise statistics
* 🕒 Recent attendance

---

## 📋 Attendance Reports

The Reports section displays attendance records from the SQLite database.

Example:

| Student ID | Name      | Date       | Time     |
| ---------- | --------- | ---------- | -------- |
| 1          | Student A | 2026-09-01 | 09:15:20 |
| 2          | Student B | 2026-09-01 | 09:17:04 |

---

## 📥 Export Attendance to Excel

The system can export attendance records to an Excel file.

The exported file is:

```text
Attendance_Report.xlsx
```

The Excel file contains:

```text
Student ID
Name
Date
Time
```

---

## 🔐 Authentication

The Flask application includes an administrator login system using Flask sessions.

> For a production deployment, credentials should be moved to environment variables or a secure authentication system rather than keeping them directly in source code.

---

## ⚠️ Requirements

Before running the face recognition features, make sure you have:

* Python 3.x
* Working webcam
* Windows/Linux/macOS system
* Sufficient lighting
* OpenCV with the contrib modules
* Required Python packages installed

---

## ⚠️ Limitations

* Recognition performance depends on lighting conditions.
* A webcam is required for face capture and attendance.
* LBPH may be less robust than modern deep-learning face recognition systems.
* New students require face-image capture and model retraining.
* The current application is primarily designed for local execution.
* Face recognition accuracy can vary based on camera quality, face angle, and image quality.

---

## 🔮 Future Improvements

Possible future improvements include:

* 🌐 Cloud database integration
* 📱 Mobile application
* 🤖 Deep-learning-based face recognition
* 📧 Email attendance notifications
* 📱 QR-code attendance
* 👨‍🎓 Student login portal
* 📊 Advanced attendance analytics
* 📹 Multi-camera support
* ☁️ Cloud deployment
* 🔒 Improved authentication and role-based access
* 🛡️ Anti-spoofing/liveness detection

---

## 🔒 Privacy & Security

This project processes biometric face images. When using it with real students:

* Obtain appropriate consent.
* Store face datasets securely.
* Do not publish students' face images publicly.
* Restrict access to attendance data.
* Follow applicable privacy and data-protection requirements.

For GitHub, the project intentionally ignores the following generated/private files:

```text
dataset/
attendance.db
trainer/
*.db
*.xlsx
```

---

## 🚀 Future Deployment

The repository includes a `Procfile` for a Gunicorn-based deployment:

```text
web: gunicorn app:app
```

However, **web deployment of this project does not automatically provide access to the user's local webcam**. The current architecture launches OpenCV webcam processes on the machine running the application.

For production deployment, the webcam/face-recognition architecture would need to be redesigned for browser-based camera capture or a dedicated client application.

---

## 👩‍💻 Developer

**Ankita**

B.Tech Computer Science Engineering

Yadavindra Department of Engineering
Punjabi University

---

## 📚 Technologies & References

* Python
* Flask
* OpenCV
* SQLite
* NumPy
* Pillow
* OpenPyXL
* Bootstrap
* JavaScript
* Chart.js

---

## ⭐ Acknowledgement

This project was developed as an academic project to demonstrate the practical application of **Artificial Intelligence, Computer Vision, Face Recognition, Database Management, and Web Development** in an automated attendance system.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
