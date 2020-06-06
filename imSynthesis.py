# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 04:28:14 2017

@author: Faculty
"""

import numpy as np
#import scipy as sc
#import pandas as pd
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import wave, struct
import csv 

import skimage.io as sk

myImage = sk.imread('mango.jpg')
sk.imshow(myImage)
myAr = np.asarray(myImage)
myShape = myAr.shape
dimR = myShape[0]//3
dimC = myShape[1]//3

smallR = myAr[0:dimR, 0:dimC, 0];
           



