import face_recognition
import cv2
import json
import numpy as np
import os

DB_FILE = "faces.json"

# Load registered faces
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        data = json.load(f)
        known_encodings = [np.array(entry["encoding"]) for entry in data]
        known_names = [entry["name"] for entry in data]
else:
    print("No registered faces found.")
    exit()

# Start webcam
video = cv2.VideoCapture(0)

print("[INFO] Starting webcam... Press Q to quit")

while True:
    ret, frame = video.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_names[index]

        # Scale back up face locations since the frame we used was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw box
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Live Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
