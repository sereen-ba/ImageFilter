# you can use this code to generates new color from the BGR set 
# in this file we are using Trackbar method and displaying our changes 

import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

    
img= np.zeros((300,300,3),np.uint8)
cv.namedWindow('control', 0)

cv.createTrackbar('B','control',0,255,nothing)
cv.createTrackbar('G','control',0,255,nothing)
cv.createTrackbar('R','control',0,255,nothing)
switch ='0 : OFF\n 1 : ON'
cv.createTrackbar(switch,'control',0,1,nothing)
while(1):
    cv.imshow('image',img)
    K=cv.waitKey(1) & 0xFF
    if K ==27 :
        break
    b=cv.getTrackbarPos('B','control')
    g=cv.getTrackbarPos('G','control')
    r=cv.getTrackbarPos('R','control')
    s=cv.getTrackbarPos(switch,'control')
    if s==0:
        img[:] = 0
    elif s==1:
        img[:] = [b,g,r]

cv.destroyAllWindows()
# Arthur:sereen bahdad
