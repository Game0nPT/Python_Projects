import cv2
import numpy as np

color = cv2.imread('cat.jpg')
cv2.imshow("Original", color)

# Using cv2.cvtColor() method 
gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
cv2.imshow("exercicio 1", gray)

# Using cv2.GaussianBlur() method 
gauss =cv2.GaussianBlur(gray, (17,17), 3.7) 
cv2.imshow("exercicio 2", gauss)

# Using cv2.medianBlur() method 
std=cv2.medianBlur(gray, 3)
cv2.imshow("exercicio 3", std)

# Using cv2.flip() method 
# Use Flip code 0 to flip vertically 
fliping=cv2.flip(gray, 0)
cv2.imshow("exercicio 4", fliping)

cv2.waitKey()