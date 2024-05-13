import cv2
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import numpy as np
import math
import pyautogui

width, heght=480, 800
X1=X2=Y1=Y2=0
cap =cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, heght)
mpHands = mp.solutions.hands
hands =mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
detector=HandDetector(detectionCon=0.5 ,maxHands=2)

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    # hands ,img=detector.findHands(img)
    # img_height, img_width, _ = img.shape
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h,w,c =img.shape
                cx,cy= int(lm.x*w), int(lm.y*h)
                # print(id,cx, cy)
                if id==4:
                    cv2.circle(img,(cx,cy), 10, (255,0,255), cv2.FILLED)
                    X1=cx
                    Y1=cy 
                if id==8:
                    cv2.circle(img,(cx,cy), 10, (255,0,255), cv2.FILLED)
                    X2=cx
                    Y2=cy
                cv2.line(img,(X1,Y1),(X2,Y2),(0,0,0),5)
                dist=((X2-X1)**2 + (Y2-Y1)**2)**(0.5)//4
                # length = math.hypot(X2-X1,Y2-Y1)
                # print (length)
                
                # if dist >25:
                #     pyautogui.hotkey('ctrl', '+')
                # else:
                #     pyautogui.hotkey('ctrl', '-')



            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    

    cv2.imshow("camera frame", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break