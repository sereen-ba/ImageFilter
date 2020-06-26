import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

    
img= np.zeros((300,512,3),np.uint8)
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




#relation operation with pixels
#img1= np.zeros((250,500,3),np.uint8)
#img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
#img2=np.zeros((250,500,3),np.uint8)
#img2=cv2.rectangle(img2,(250,0),(500,250),(255,255,255),-1)
#bitAnd=cv2.bitwise_and(img2,img1)
#bitOr=cv2.bitwise_or(img2,img1)
#bitXor=cv2.bitwise_xor(img2,img1)  
#cv2.imshow('first',img1)
#cv2.imshow('second',img2)
#cv2.imshow('bitOr',bitOr)
#cv2.imshow('bitAnd',bitAnd)
#cv2.imshow('bitOr',bitXor)

cv.destroyAllWindows()
