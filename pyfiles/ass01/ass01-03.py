'''
Created on 15 Nov 2016

@author: Kumori
'''
import numpy as np
import cv2
import math
import random

def wuerzenAlt (input, n):
    height, width = input.shape
    spicedPixels = int(height * width * n)
    output = input
    spicedCounter = 0
    print 'The spiced Pixels are over: ', spicedPixels
    spicer = 0
    while (spicedCounter < spicedPixels):
       
        for y in range(0,height):
            for x in range(0,width):
                spicer = random.randint(0,2)
                #print spicer, ''
                if(spicer==0 and spicedCounter < spicedPixels):
                    output.itemset((y,x),0)
                    spicedCounter = spicedCounter + 1
                   # print 'Pepper'
                elif(spicer==1 and spicedCounter < spicedPixels):
                    output.itemset((y,x),255)
                    spicedCounter = spicedCounter +1
                    #print 'Salty'
                else:
                    #print 'Unspiced'
                    foo = 1
                  
    print spicedCounter
    return output   

def wuerzen (input , n):
    height, width = input.shape
    spicedPixels = int(height * width * n)
    output = input.copy()
    
    for i in range(0,spicedPixels):
        output.itemset(random.randint(0,height-1), random.randint(0,width-1), random.randint(0,1)*255)
    
    return output

def ssd(unSpiced, spiced):
    height, width = unSpiced.shape
    result = 0
    for y in range(0,height):
            for x in range(0,width):
             result = result + math.pow(unSpiced.item(y,x) - spiced.item(y,x),2)
             
             
    #print 'squared sum difference: ', result
    return result


inputImg = cv2.imread('lena.pgm',0)
outputImg = wuerzen(inputImg, 0.05)

cv2.imshow('Spiced Lena',outputImg)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()

cv2.imshow('Unspiced Lena',inputImg)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()

print'ssdtest: ', ssd(inputImg, inputImg)
print 'ssdreal: ', ssd(inputImg, outputImg)
