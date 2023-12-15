import sys
import os
venv_path = 'venv\Lib\site-packages'
sys.path.insert(0, venv_path)

import cv2
from deepface import DeepFace
from imspecifications import specifications

img_path = 'images\young_girl.jpg'

detected_faces = DeepFace.extract_faces(img_path)  #detects face in image
attributes = DeepFace.analyze(img_path, actions = ['gender', 'age', 'race', 'emotion'])  #analyzes specified attributes

#print(attributes)

if detected_faces:    #checks if any faces were detected

    img = cv2.imread(img_path)

    for face in detected_faces:   #put a bounding box around each detected face (and text)

        face1 = face.get('facial_area')    

        if face1:
            x, y, w, h = face1['x'], face1['y'], face1['w'], face1['h']

            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            specifications(img_path, img, x, y, h)

    cv2.imshow('Detected Faces', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print('No faces were detected in the provided image.')
