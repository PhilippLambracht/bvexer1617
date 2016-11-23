'''
Created on 22 Nov 2016

@author: Kumori
'''
import numpy as np
import cv2
import math
from cmath import sqrt


kern = np.array( [ [0.0039062, 0.0156250, 0.0234375, 0.0156250, 0.0039062],
                 [0.0039062, 0.0156250, 0.0234375, 0.0156250, 0.0039062],
                 [0.0234375, 0.0937500, 0.1406250, 0.0937500, 0.0234375],
                 [0.0156250, 0.0625000, 0.0937500, 0.0625000, 0.0156250],
                 [0.0039062, 0.0156250, 0.0234375, 0.0156250, 0.0039062] ])



def boderFixing(yVal,xVal,yMax,xMax):
    if (yVal < 0):
        yVal = yVal * (-1)
    if (xVal < 0):
        xVal = xVal * (-1)
    if (yVal >= yMax):
        yVal = yMax - (yVal-yMax)
    if (xVal >= xMax):
        xVal = xMax - (xVal-xMax)        
    return yVal, xVal

def genMeanKernel(n):
    meany = np.full((n,n),1.0/n)
    #print meany
    return meany
    
def filterFixed(input, filter):
    output = input.copy()
    height, width = input.shape
    fHeight, fWidth = filter.shape
    fMiddleHeight = fHeight/2
    fMiddleLength = fWidth/2
    
    for y in range(0,height):
            for x in range(0,width):
                n = fHeight/2 *(-1)
                m = fWidth/2 * (-1)
                
                for fy in range(0,fHeight):
                    for fx in range(0,fWidth):
                        if(y+n >=0 and y+n < height and x+m  >= 0 and x+m < width):
                            output.itemset((y,x), output.item(y,x) + (input.item(y+n,x+m) * filter.item(fy,fx)) )
                           # print  'Orig Val : ', input.item(y,x), ' changed Val: ', output.item(y,x)
                        else:
                            foo =1
                        m = m+1
                    
                    n = n + 1
    
    
    return output

def filterFixedFull(input, filter):
    output = input.copy()
    height, width = input.shape
    fHeight, fWidth = filter.shape
    fMiddleHeight = fHeight/2
    fMiddleLength = fWidth/2
    
    for y in range(0,height):
            for x in range(0,width):
                n = fHeight/2 *(-1)
                m = fWidth/2 * (-1)
                
                for fy in range(0,fHeight):
                    for fx in range(0,fWidth):
                        modYVal = y+n
                        modXVal = x+m
                        #print 'height, width: ', height-1, width-1
                        
                        #print 'Unchanged y,x: ',modYVal ,modXVal
                        modYVal, modXVal = boderFixing(modYVal,modXVal,height-1,width-1)
                        #print 'changed y,x: ',modYVal ,modXVal
                        if(modYVal >=0 and modYVal < height and modXVal  >= 0 and modXVal < width):
                            output.itemset((y,x), output.item(y,x) + (input.item(modYVal,modXVal) * filter.item(fy,fx)) )
                           # print  'Orig Val : ', input.item(y,x), ' changed Val: ', output.item(y,x)
                        else:
                           print 'upps'
                        m = m+1
                    
                    n = n + 1
    
    
    return output
    
genMeanKernel(15)  
inputImg = cv2.imread('lena.pgm',0)
mean17 =  genMeanKernel(5)
print mean17.shape
print mean17

# outputImg = filterFixed(inputImg, kern)
outputImg2 = filterFixedFull(inputImg, kern)
outputImg3 = filterFixedFull(inputImg, mean17)

cv2.imshow('Unfiltered Lena',inputImg)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()
'''
cv2.imshow('Filteret Lena unfixed',outputImg)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()
'''
cv2.imshow('Filteret Lena unfixed',outputImg2)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()

cv2.imshow('Filteret Lena mean',outputImg3)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()
