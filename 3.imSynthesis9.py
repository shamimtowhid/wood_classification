# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 04:28:14 2017

@author: Faculty
"""
from PIL import Image
import numpy as np
import os
#import matplotlib.pyplot as plt
import skimage.io as sk
import re


        
def Synthesize_and_save(filename,original_name):
    myImage = sk.imread('images/'+original_name)
    myArr=np.asarray(myImage)
    myShape=myArr.shape
    dimR=myShape[0]//3
    dimC=myShape[1]//3
    for ii in range (0,3):
        for jj in range(0,3):           
            small = myArr[ii*dimR:(ii+1)*dimR, jj*dimC:(jj+1)*dimC];
            im = Image.fromarray(small)
            newfilename=filename.split(".",1)[0]
            im.save('Dataset/'+newfilename+str(ii*3+jj)+'.jpg')
    print("Successfully Saved")
    
if __name__=="__main__":
    images_list = os.listdir('./images/')
    h=1
    for image in images_list:
        print("processing image no:",h)
        string_name2=re.sub(r"^\['",'',str(image))
        string_name1=re.sub("'",'',str(string_name2))
        string_name=re.sub("]",'',str(string_name1))
        Synthesize_and_save(string_name,str(image))
        h=h+1

        