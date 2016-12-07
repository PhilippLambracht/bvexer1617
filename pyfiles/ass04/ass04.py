'''
Created on 7 Dec 2016

@author: Kumori
'''

import numpy as np
import cv2
import math
import random


def histogramm(inImage):
    hist = np.zeros((255),dtype=np.int)
    height, width = inImage.shape
    #print hist
    for y in range(0,height):
            for x in range(0,width):
                histIndex = inImage.item(y,x) 
                hist.itemset(histIndex, hist.item(histIndex) + 1)
                
    
    #print hist
    return hist
    
def printhist(hist):
    greyVal = 0
    for i in hist:
        print 'Grauwert: ', greyVal, ' Anzahl: ', i
        greyVal = greyVal + 1
        

def creatInverseLUT():
    lut = np.arange(256,dtype=np.int)
    lut = np.flipud(lut)
    #print lut
    return lut
    

def apply_lut(inImage, lut):
    height, width = inImage.shape
    output = np.zeros((height,width), np.uint8)
    
    for y in range(0,height):
            for x in range(0,width):
                lutVal= lut.item(inImage.item(y,x))
                #print lutVal
                #print 'y: ', y, 'x: ',x
                output.itemset((y,x),lutVal)
    
    return output

def hist_spread_lut(hist):
    min = 255
    max = 0
    maximum = 255.0
    minimum = 0.0
    #printhist(hist)
    lut = np.arange(256,dtype=np.int)
    index = 0
    for i in hist:
        #print 'iees: ', i
        if (i > 0) and (index<min):
            #print 'index : ', index, ' i: ',i ,' oldMin: ' , min
            min = index
            #print 'index : ', index, ' newdMin: ' , min
        if (i > 0) and (index>max):
            #print 'index : ', index, ' i: ',i ,' oldMin: ' , min
            max = index
            #print 'index : ', index, ' newdMin: ' , min
            
        index = index + 1 
    
    print 'min: ', min , ' max: ', max
    index = 0
    for v in range(min,max):
        #print 'Bruch : ',(maximum-minimum)/(max-min)
        lutVal = minimum + (v-min) * ((maximum-minimum)/(max-min))
        #print lutVal
        lut.itemset(index,lutVal)
        index = index + 1
    print lut
    return lut

inputImg = cv2.imread('lena.pgm',0)
hist =histogramm(inputImg)
#printhist(hist)
inverseLut = creatInverseLUT()
spreadLut = hist_spread_lut(hist)

inverseImg = apply_lut(inputImg, inverseLut)
spreadImg = apply_lut(inputImg, spreadLut)

spreadHist = histogramm(spreadImg)
printhist(spreadHist)

cv2.imshow('Normal',inputImg)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()

cv2.imshow('Inverse',inverseImg)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()

cv2.imshow('Spread',spreadImg)
cv2.waitKey(0)& 0xFF
cv2.destroyAllWindows()


    
    
    
    
    