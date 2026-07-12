import cv2
import os
import numpy as np
from PIL import Image

# Create LBPH Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

dataset_path = "dataset"

faces = []
ids = []

# Read all images from dataset
for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)

    if os.path.isdir(folder_path):
        try:
            student_id = int(folder.split("_")[-1])
        except:
            continue

        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)

            img = Image.open(image_path).convert('L')
            img_np = np.array(img, 'uint8')

            faces.append(img_np)
            ids.append(student_id)

# Train model
recognizer.train(faces, np.array(ids))

# Create trainer folder if not exists
os.makedirs("trainer", exist_ok=True)

# Save trained model
recognizer.save("trainer/trainer.yml")

print("Training completed successfully!")