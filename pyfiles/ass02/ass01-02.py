'''
Created on 14.11.2016

@author: MothSlayer
'''

import numpy as np
import cv2

def mittelwert(img):
    sum = 0
    n = 0
    x = 0
    y = 0
    height, width = img.shape
    for y in range(0,height):
        for x in range(0,width):
            sum = sum + img.item(y,x)
            n = n +1
    print 'Mittelwert: ', sum/n
    
def varianz(img):
    sum = 0
    n = 0
    x = 0
    y = 0
    height, width = img.shape
    for y in range(0,height):
        for x in range(0,width):
            sum = sum + img.item(y,x)
            n = n +1
    print 'Varianz: ', sum/n


    
    
    
            

img = cv2.imread('lena.pgm',0)
img = mittelwert (img)

