##import sys
##import os
##venv_path = 'venv'
##sys.path.insert(0, venv_path)

import cv2
from deepface import DeepFace

def vspecifications(frame, x, y, h):   #puts text on image
    attributes = DeepFace.analyze(frame, actions = ['gender', 'age', 'race', 'emotion'])

    if attributes:
                for specs in attributes:

                    #extract info from dictionary inside a list
                    gender = specs['dominant_gender']       
                    age = specs['age']
                    race = specs['dominant_race']
                    emotion = specs['dominant_emotion']

                    text1 = f'Gender: {gender}'
                    text2 = f'Age: {age}'
                    text3 = f'Race: {race}'
                    text4 = f'Emotion: {emotion}'

                    text = [text1, text2, text3, text4]
                    
                    i = 0
                    c = 60
                    while i<len(text):
                            cv2.putText(frame, text[i], (x,y+h+c), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1) #puts each attribute in its own line
                            i+=1
                            c+=30
    else:
         print("Failed to analyze face.")
