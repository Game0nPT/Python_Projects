import cv2
import numpy as np


#exerc1
color = cv2.imread('cat.jpg')
cv2.imshow("color", color)

original = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", original)


#exerc2
gauss = cv2.GaussianBlur(original, (17,17), 3.7)
cv2.imshow("2", gauss)


#exerc3
median = cv2.medianBlur(original, 3)
cv2.imshow("3", median)


#exerc4
flip_x = cv2.flip(original, 0)
cv2.imshow("4", flip_x)


#exerc5
Z = -50

rows = original.shape[0]
print("rows=", rows)
cols = original.shape[1]
print("cols=", cols)

brightness = np.zeros((original.shape), np.uint8)
# or
#brightness = original[:]

#print(id(brightness)) #checking if they are diferent objects  
#print(id(original))

# it is not the faster option:
for i in range(rows): 
    for j in range(cols):
        v = original.item(i,j)
        
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
        
#OR
#br = np.clip(original + Z, 0, 255)
#br = br.astype(np.uint8)
#cv2.imshow("5 & 6_", br)

#OR
#It is the faster option:
#br2 = cv2.add(original , Z)
#cv2.imshow("br2", br2)

cv2.imshow("5 & 6", brightness)

#exerc7
flip_xx = np.zeros((original.shape), np.uint8)
i = rows-1
for line in original:
    flip_xx[i] = line
    i -= 1

cv2.imshow("7", flip_xx)


#exerc8
Ln = original.shape[0] 
Col = original.shape[1]
flip_yy = np.zeros((Col, Ln), np.uint8) # rows is given by  cols of original

temp = np.transpose(original) # from here the original columns are treated 
                              # as rows
i = cols-1
for line in temp:
    flip_yy[i] = line
    i -= 1

flip_yy = np.transpose(flip_yy) # recovering the original shape

cv2.imshow("8", flip_yy)


#exerc9
roi = original[22:22+60, 30:30+285]
cv2.imshow("9a", roi)


#exerc10
lap = cv2.Laplacian(original, 8)
cv2.imshow("10", lap)


#exerc11
cir = np.copy(original)
cir = cv2.cvtColor(cir, cv2.COLOR_GRAY2BGR)
cir = cv2.circle(cir, (int(cols/2), int(rows/2)), 50, (0,255,0), 4)
cv2.imshow("11", cir)


#exerc12
sobel1 = [ [1.0, 2.0 ,1.0], [0.0, 0.0 ,0.0], [-1.0, -2.0, -1.0]  ]
k = np.array(sobel1)
sob = cv2.filter2D(original, 8, k)
cv2.imshow("12", sob)
cv2.waitKey()


#exerc13
def noise(img, n):
   
    nRows = img.shape[0]
    nCols = img.shape[1]
    
    r = np.random.randint(nRows, size=n)
    c = np.random.randint(nCols, size=n)

    for i in range(n):
        img.itemset((r[i],c[i]), 255 )


noiseImg = original.copy()
noise(noiseImg, 10000)  # add noise
cv2.imshow("noise", noiseImg)

filt = cv2.medianBlur(noiseImg, 3) # remove noise
cv2.imshow("w/noise", filt)
cv2.waitKey()

