import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

        ret, frame = cap.read()

        frame = cv2.GaussianBlur(frame, (7,7), 1.9)

        cv2.imshow("color", frame)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", gray)
        
        edges = cv2.Canny(gray, 50, 100)
        cv2.imshow("edges", edges)
        
        cv2.waitKey(10)