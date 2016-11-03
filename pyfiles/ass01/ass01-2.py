'''
Created on 03.11.2016

@author: MothSlayer
'''

import numpy as np
import cv2




#Aufgabe 2
def graukeil (gkeil):
    
    x=0
    y=0
    grey = 0
    height, width = gkeil.shape #get height and width of image
    while (y < height):
        while (x < width):
            gkeil.itemset((y,x),grey)
            x += 1
            grey +=1
            #print y, x, grey
        x=0
        grey = 0
        y +=1
        
    return gkeil    
    

def blackframe(bframe):
    x=0
    y=0
    value = 0
    height, width = bframe.shape #get height and width of image
    while (y < height):
        while (x < width):
            if (x==5 and y>=5 and y<=height-5) or (x==width-5 and y>=5 and y<=height-5) or (y==5 and x>=5 and x <=width-5) or (y==height-5 and x>=5 and x <=width-5):
                bframe.itemset((y,x),value)
            x+= 1    
        x=0
        
        y += 1
            
    return bframe


height= 400
width = 300

#create blank image
blankImg = np.zeros((height,width,1), np.uint8)
cv2.imwrite('blankImg.pgm',blankImg)

# create graukeil
keil = cv2.imread('blankImg.pgm',0)
keil = graukeil (keil)

# safe and show Image
cv2.imwrite('graukeil.pgm',keil)
cv2.imshow('graukeil',keil)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()

#create white image
whiteImg =np.full((height,width,1),255,np.uint8)
cv2.imwrite('whiteBlank.pgm',whiteImg)

bframe= cv2.imread('whiteBlank.pgm',0)
bframe = blackframe(bframe)

cv2.imwrite('blackframe.pgm',bframe)
cv2.imshow('blackFrame',bframe)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()

    
# img = cv2.imread('opencv_screenshot.jpg', 0)

# cv2.imwrite('testor.jpg',img)
# cv2.imshow('',img)
# cv2.waitKey(0)& 0xFF
# cv2.destroyAllWindows()

