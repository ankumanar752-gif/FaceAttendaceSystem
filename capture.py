import cv2
import os

# Ask for student details
import sys

student_id = sys.argv[1]
student_name = sys.argv[2]

# Create folder
folder = f"dataset/{student_name}_{student_id}"
os.makedirs(folder, exist_ok=True)

# Load face detector
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    # Save faces
    for (x, y, w, h) in faces:
        count += 1

        face = gray[y:y+h, x:x+w]

        cv2.imwrite(f"{folder}/{count}.jpg", face)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame, str(count), (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Capture Face", frame)

    if cv2.waitKey(1) & 0xFF == 27 or count >= 50:
        break

cap.release()
cv2.destroyAllWindows()

print("Face images captured successfully!")