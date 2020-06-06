# -*- coding: utf-8 -*-
import numpy as np
#import matplotlib.pyplot as plt
import csv 
#from PIL import Image
import skimage.io as sk
import pandas as pd
from addNoise import synthesize

nLevels = 30
nFeats = 5*4*3
nClass = 50
nImages = nClass*9*3

texture = np.zeros((nImages, nFeats+1))

csvf = pd.read_csv ('woodClass.csv', sep=",", header=None)

for totalcontrol in range(0,nClass):
    csvName = csvf.loc[totalcontrol][0]
    csvClass = csvf.loc[totalcontrol][1]
    print('processing filenumber ',totalcontrol)
    
    name = csvName.split(".",1)[0]
    for si in range(0,9):     
        fname = name + str(si)+".jpg"
    
        texImage = sk.imread('Dataset/'+fname)
        texArr = np.asarray(texImage)
        texShape = texArr.shape
        height = texShape[0]
        width = texShape[1]
        
        for u in range(0,3):
            if u==0:
                texArr_noise=texArr
            else:
                textArr_noise=synthesize(texArr,height,width)
        
            for ci in range(0, 3):
                fr = (totalcontrol*27)+(si*3)+u
                fc = ci*20
                cArr = texArr_noise[:, :, ci]
                coarseSyl = np.zeros((height,  width ))
                cMax = np.max(cArr)
                for r in range(0, height):
                    for c in range(0, width):
                        scaledVal = (cArr[r][c]/cMax) * (nLevels-1)
                        coarseSyl[r][c]=np.round(scaledVal)
                        
                nSteps = int(np.max(coarseSyl)+1) 
                
                glcm0 = np.zeros((nSteps, nSteps)) 
                for r in range(0, height):
                    for c in range(0, width-1):
                        pp = int(coarseSyl[r][c])
                        p10 = int(coarseSyl[r][c+1])
                        glcm0[pp][p10]=glcm0[pp][p10]+1       
                             
                glcm45 = np.zeros((nSteps, nSteps)) 
                for r in range(0, height-1):
                    for c in range(0, width-1):
                        pp = int(coarseSyl[r][c])
                        p10 = int(coarseSyl[r+1][c+1])
                        glcm45[pp][p10]=glcm45[pp][p10]+1
                              
                glcm90 = np.zeros((nSteps, nSteps)) 
                for r in range(0, height-1):
                    for c in range(0, width):
                        pp = int(coarseSyl[r][c])
                        p10 = int(coarseSyl[r+1][c])
                        glcm90[pp][p10]=glcm90[pp][p10]+1
                              
                glcm135 = np.zeros((nSteps, nSteps)) 
                for r in range(0, height-1):
                    for c in range(0, width-1):
                        pp = int(coarseSyl[r][c])
                        p10 = int(coarseSyl[r+1][c-1])
                        glcm135[pp][p10]=glcm135[pp][p10]+1
                              
                glcm0 = glcm0/np.sum(glcm0)
                glcm45 = glcm45/np.sum(glcm45)
                glcm90 = glcm90/np.sum(glcm90)
                glcm135 = glcm135/np.sum(glcm135)
                
                logConst = 0.01
                
                texture[fr][fc+0] = np.sum(glcm0*glcm0)
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + r*glcm0[r][c]
                mean = mSum
                
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-mean)*(r-mean)*glcm0[r][c]
                sigma2 = mSum
                if sigma2==0:
                    sigma2=0.0001
                
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-mean)*(c-mean)*glcm0[r][c]
                texture[fr][fc+1] = mSum/sigma2
        
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-c)*(r-c)*glcm0[r][c]
                texture[fr][fc+2] = mSum
                       
                texture[fr][fc+3] = - np.sum(glcm0*np.log(logConst+np.abs(glcm0)))  
        
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + glcm0[r][c]/(1+(r-c)*(r-c))
                        
                texture[fr][fc+4] = mSum
        
            # Direction 45
                texture[fr][fc+5] = np.sum(glcm45*glcm45)
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + r*glcm45[r][c]
                mean = mSum
                
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-mean)*(r-mean)*glcm45[r][c]
                sigma2 = mSum
                if sigma2==0:
                    sigma2=0.0001
                
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-mean)*(c-mean)*glcm45[r][c]
                texture[fr][fc+6] = mSum/sigma2
        
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-c)*(r-c)*glcm45[r][c]
                texture[fr][fc+7] = mSum
                       
                texture[fr][fc+8] = - np.sum(glcm45*np.log(logConst+np.abs(glcm45)))  
        
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + glcm45[r][c]/(1+(r-c)*(r-c))
                        
                texture[fr][fc+9] = mSum
        
            # Direction 90
                texture[fr][fc+10] = np.sum(glcm90*glcm90)
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + r*glcm90[r][c]
                mean = mSum
                
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-mean)*(r-mean)*glcm90[r][c]
                sigma2 = mSum
                if sigma2==0:
                    sigma2=0.0001
        
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-mean)*(c-mean)*glcm90[r][c]
                texture[fr][fc+11] = mSum/sigma2
        
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-c)*(r-c)*glcm90[r][c]
                texture[fr][fc+12] = mSum
                       
                texture[fr][fc+13] = - np.sum(glcm90*np.log(logConst+np.abs(glcm90)))  
        
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + glcm90[r][c]/(1+(r-c)*(r-c))
                        
                texture[fr][fc+14] = mSum
                    
             # Direction 135
                texture[fr][fc+15] = np.sum(glcm135*glcm135)
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + r*glcm135[r][c]
                mean = mSum
                
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-mean)*(r-mean)*glcm135[r][c]
                sigma2 = mSum
                if sigma2==0:
                    sigma2=0.0001
        
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-mean)*(c-mean)*glcm135[r][c]
                texture[fr][fc+16] = mSum/sigma2
        
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + (r-c)*(r-c)*glcm135[r][c]
                texture[fr][fc+17] = mSum
                       
                texture[fr][fc+18] = - np.sum(glcm135*np.log(logConst+np.abs(glcm135)))  
        
                mSum = 0
                for r in range(0, nSteps):
                    for c in range(0, nSteps):
                        mSum = mSum + glcm135[r][c]/(1+(r-c)*(r-c))
                        
                texture[fr][fc+19] = mSum   
            texture[fr][60] = csvClass
            
   
    
appendedList=np.zeros(61)

fn = 'features/features.csv'
with open(fn, 'w', newline='') as f:
    out=csv.writer(f,delimiter=',',quoting=csv.QUOTE_ALL)
    for frow in range(0,nImages):
        for fcol in range(0,61):
            appendedList[fcol]=texture[frow][fcol]
            if fcol==60:
                out.writerow(appendedList)
    f.close()
    
    
                # appendedList[:]=[]     # not necessary but good practice
    #cmap=gnuplot



    #plt.subplot(4,1,4)
    #deng = np.diff(eng)
    #plt.plot(deng)
    #plt.show()
    #



