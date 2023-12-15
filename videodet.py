import sys
import os
venv_path = 'venv\Lib\site-packages'
sys.path.insert(0, venv_path)

import cv2
from deepface import DeepFace
from vidspecifications import vspecifications

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Failed to open camera.")
    
    detected_faces = DeepFace.extract_faces(frame)

    for face in detected_faces:   #put a bounding box around each detected face

        face1 = face.get('facial_area')    

        if face1:
            x, y, w, h = face1['x'], face1['y'], face1['w'], face1['h']
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        vspecifications(frame, x, y, h)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    