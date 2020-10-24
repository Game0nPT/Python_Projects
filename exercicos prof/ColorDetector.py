import cv2
import numpy as np


mXY = [-1,-1]  

def mousexy(event, x, y, flags, param): # function to handle the mouse events

    global mXY # mouse x y     
   
    if event == cv2.EVENT_LBUTTONDOWN:
        mXY = [x, y]
      
    


cv2.namedWindow('frame')
cv2.setMouseCallback('frame', mousexy) #set the function callback to the window frame


targetColor = np.array([160, 189, 133])
margins = np.array([45,40,50])

#define the initial target range using the target color and the margins
lower_range = np.array(np.clip(targetColor - margins, 0, 255), dtype=np.uint8)
upper_range = np.array(np.clip(targetColor + margins, 0, 255), dtype=np.uint8)

cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.GaussianBlur(frame, (7,7), 1.7)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL) # work on the HSV color space is more comprehensible for us


    if mXY[0] != -1:  #getting a new pixel sample - a new mouse click happened

            targetColor = hsv[ mXY[1] ][ mXY[0] ] # define the new color target
            
            #compute the new range
            lower_range = np.array(np.clip(targetColor - margins, 0, 255), dtype=np.uint8)
            upper_range = np.array(np.clip(targetColor + margins, 0, 255), dtype=np.uint8)
            
            mXY = [-1,-1] # reset the mouse marker


    mask = cv2.inRange(hsv, lower_range, upper_range)    # search for the pixels which are into the range
                                                         # at the same time paint the mask image with white pixels for that case 

    #find the contours for the detected regions 
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 

    C = [ct for ct in contours if ct.size > 50]  # List comprehension to get contours where its size is greater than 50
    
    frame = cv2.drawContours(frame, C, -1, (0,255,0), 3) # draw the contours
                
    cv2.imshow('mask',mask)
    
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    ch = cv2.waitKey(10) & 0xFF
    if  ch == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

