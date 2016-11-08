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

def chessfield(cfield, n):
    x=0
    y=0
    height, width = cfield.shape
    white = 255
    black = 0
    ySideSwitch = False
    xSideSwitch = False
    for y in range(0,height):
        for x in range(0,width):
            
            
            if (ySideSwitch==False and xSideSwitch==True):
                cfield.itemset((y,x),white)
            else:
                cfield.itemset((y,x),black)
            
            if((x % n ==0) and (x>0)):
                xSideSwitch = not xSideSwitch
            
        if((y % n == 0) and (y>0)):
            ySideSwitch = not ySideSwitch
            
    return cfield       
    
ImgHeight= 400
ImgWidth = 300

#create blank image
blankImg = np.zeros((ImgHeight,ImgWidth,1), np.uint8)
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
whiteImg =np.full((ImgHeight,ImgWidth,1),255,np.uint8)
cv2.imwrite('whiteBlank.pgm',whiteImg)

bframe = cv2.imread('whiteBlank.pgm',0)
bframe = blackframe(bframe)

cv2.imwrite('blackframe.pgm',bframe)
cv2.imshow('blackFrame',bframe)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()

blankchess =np.full((200,200,1),255,np.uint8)
cv2.imwrite('blankchess.pgm',blankchess)

chessf = cv2.imread('blankchess.pgm',0)
print chessf.shape
chessf = chessfield(chessf, 50)


cv2.imwrite('chessfield.pgm',chessf)
cv2.imshow('chessfield',chessf)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()


# img = cv2.imread('opencv_screenshot.jpg', 0)

# cv2.imwrite('testor.jpg',img)
# cv2.imshow('',img)
# cv2.waitKey(0)& 0xFF
# cv2.destroyAllWindows()

