import cv2
import numpy as np


color = cv2.imread('cat.jpg')
cv2.imshow("Original", color)

#exercico 1
# Using cv2.cvtColor() method 
gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
cv2.imshow("exercicio 1", gray)

#exercico 2
# Using cv2.GaussianBlur() method 
gauss =cv2.GaussianBlur(gray, (17,17), 3.7) 
cv2.imshow("exercicio 2", gauss)

#exercico 3
# Using cv2.medianBlur() method 
std=cv2.medianBlur(gray, 3)
cv2.imshow("exercicio 3", std)

#exercico 4
# Using cv2.flip() method 
# Use Flip code 0 to flip vertically 
fliping=cv2.flip(gray, 0)
cv2.imshow("exercicio 4", fliping)


#exercico 5

Z = -50

rows = gray.shape[0]
print("rows=", rows)
cols = gray.shape[1]
print("cols=", cols)

brightness = np.zeros((gray.shape), np.uint8)
for i in range(rows): 
    for j in range(cols):
        v = gray.item(i,j)
        #exerc6
        if v+Z > 255:
            o = 255
        elif v+Z < 0:
            o = 0
        else:
            o = v+Z
        
        #OR
        #o = np.clip(v+Z, 0, 255)
        
        brightness.itemset((i,j), o )
cv2.imshow("exercicio 5 e 6", brightness)

cv2.waitKey()