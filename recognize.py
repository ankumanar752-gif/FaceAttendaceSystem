import cv2
import sqlite3
from datetime import datetime

# -------------------------------
# Load Face Recognizer
# -------------------------------
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    "haarcascade/haarcascade_frontalface_default.xml"
)

# Connect Database
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Open Webcam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

font = cv2.FONT_HERSHEY_SIMPLEX

print("Face Recognition Started...")
print("Press ESC to Exit")

while True:

    ret, frame = cam.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        student_id, confidence = recognizer.predict(
            gray[y:y+h, x:x+w]
        )

        # Convert confidence to percentage
        accuracy = round(100 - confidence)

        if confidence < 70:

            cursor.execute(
                "SELECT name FROM students WHERE id=?",
                (student_id,)
            )

            student = cursor.fetchone()

            if student:

                name = student[0]

                # Draw Green Rectangle
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x+w, y+h),
                    (0, 255, 0),
                    2
                )

                # Display Name + Accuracy
                cv2.putText(
                    frame,
                    f"{name} ({accuracy}%)",
                    (x, y-10),
                    font,
                    0.8,
                    (0, 255, 0),
                    2
                )

                # Current Date & Time
                now = datetime.now()
                today = now.strftime("%Y-%m-%d")
                current_time = now.strftime("%H:%M:%S")

                # Check if already marked today
                cursor.execute(
                    """
                    SELECT *
                    FROM attendance
                    WHERE student_id=? AND date=?
                    """,
                    (student_id, today)
                )

                already_marked = cursor.fetchone()

                if already_marked is None:

                    cursor.execute(
                        """
                        INSERT INTO attendance
                        (student_id, name, date, time)
                        VALUES (?, ?, ?, ?)
                        """,
                        (
                            student_id,
                            name,
                            today,
                            current_time
                        )
                    )

                    conn.commit()

                    print(f"Attendance Marked : {name}")

                    # Prevent repeated insert
                    cv2.waitKey(1000)

            else:

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x+w, y+h),
                    (0, 0, 255),
                    2
                )

                cv2.putText(
                    frame,
                    "Unknown",
                    (x, y-10),
                    font,
                    0.8,
                    (0, 0, 255),
                    2
                )

        else:

            cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                (0, 0, 255),
                2
            )

            cv2.putText(
                frame,
                "Unknown",
                (x, y-10),
                font,
                0.8,
                (0, 0, 255),
                2
            )

    cv2.imshow("Face Attendance System", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cam.release()
conn.close()
cv2.destroyAllWindows()