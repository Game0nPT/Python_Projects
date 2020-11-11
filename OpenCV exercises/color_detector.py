import cv2
import numpy as np

mXY=[-1,-1]

def mouseXY(event, x, y, flags, param):
    global mXY
    if event == cv2.EVENT_LBUTTONDOWN:
        mXY=[x,y]

cv2.namedWindow("frame")
cv2.setMouseCallback('frame', mouseXY)

#1º argumento=lista contedo os tres valores de HSV
targetColor = np.array([160 , 189 , 133])  
margin = np.array([45 , 40 , 50])

lower_range = np.array( np.clip( targetColor - margin, 0, 255 ), dtype=np.uint8)
upper_range = np.array( np.clip( targetColor + margin, 0, 255 ), dtype=np.uint8)

cap = cv2.VideoCapture(0)

while (True):
    
    ret, frame = cap.read()

    #remover barulho
    frame = cv2.GaussianBlur(frame, (7,7), 1.7)
    #o FULL é para normalizar os hsv values
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)

    if mXY[0] != -1:
        #                  |->ESTE REFERE A POSIÇÃO DO Y, ENQUATO QUE O A SEGUIR EQUIVALE AO x
        targetColor = hsv[ mXY[1] ] [ mXY[0] ]
        lower_range = np.array( np.clip( targetColor - margin, 0, 255 ), dtype=np.uint8)
        upper_range = np.array( np.clip( targetColor + margin, 0, 255 ), dtype=np.uint8)
        mXY = [-1 ,-1]

    mask = cv2.inRange(hsv, lower_range, upper_range)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    C = [ct for ct in contours if ct.size > 250]
    
    frame = cv2.drawContours(frame, C, -1, (0,255,0), 3) # draw the contours

    cv2.imshow('mask' ,mask)
    
    cv2.imshow('frame' ,frame)
    
    ch = cv2.waitKey(10) & 0xFF
    if ch == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

