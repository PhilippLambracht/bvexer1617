'''
Created on 03.11.2016

@author: MothSlayer
'''

import numpy as np
import cv2


width = 100
height= 100


def graukeil (height, width):
    
    blankImg = np.zeros((height,width,1), np.uint8)
    cv2.imwrite('blankImg.pgm',blankImg)
    gkeil = cv2.imread('blankImg.pgm',0)
   
    
    x=0
    y=0
    grey = 0
    
    while (y < height):
        while (x < width):
            gkeil.itemset((y,x),grey)
            x += 1
            grey +=1
            print y, x, grey
        x=0
        grey = 0
        y +=1
        
        
    cv2.imwrite('graukeil.pgm',gkeil)
    print "Funktion aufgerufen"
    cv2.imshow('graukeil',gkeil)
    cv2.waitKey(0)& 0xFF
    cv2.destroyAllWindows()

graukeil (100,255)

    
# img = cv2.imread('opencv_screenshot.jpg', 0)

# cv2.imwrite('testor.jpg',img)
# cv2.imshow('',img)
# cv2.waitKey(0)& 0xFF
# cv2.destroyAllWindows()

