import cv2
import numpy as np

color = cv2.imread('cat.jpg')
cv2.imshow("Original", color)

original = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
cv2.imshow("exercicio 1", original)


gauss =cv2.GaussianBlur(original, (17,17), 3.7) 
cv2.imshow("exercicio 2", gauss)


std=cv2.medianBlur(original, 3)
cv2.imshow("exercicio 3", std)

cv2.waitKey()