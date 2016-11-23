'''
Created on 14 Nov 2016

@author: Kumori
'''

import numpy as np
import cv2
import math
from cmath import sqrt




# print np.random.normal(mu,sigma,5)
#print np.exp(3)


def gaussDistri(mu,sigma, x):
    # print mu, sigma, x
    
    result = 1 / (sigma * math.sqrt(2 * math.pi)) * np.exp( (-1) * (math.pow(x - mu, 2) / 2*math.pow(sigma,2) ))
    return result
    

def gaussmask1D(n):
    
    mu = 0.0
    sigma = 1.0
    border = 2.0 * sigma
   # print i
    step = n/2
    growth = float(border / step)
    i = mu
    #print step, growth
    xVals =[]
    result =[]
    while (i >= border * (-1.0)):
        #print i
        xVals.append(i)
        i = i - growth
    
    xVals.reverse()
    xVals.pop()
    #print xVals
    
    i = mu
    while (i <= border):
        #print i, border
        xVals.append(i)
        i = i + growth
    
    #print xVals
    
    for value in xVals:
        result.append(gaussDistri(mu, sigma, value))    
    
    #print result
    return result
        
    

 # print gaussDistri(0, 1, 0.9)
gauss1D = gaussmask1D(7)
print gauss1D


    