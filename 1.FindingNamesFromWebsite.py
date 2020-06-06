#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 23:34:55 2017

@author: shamim
"""

import requests,bs4,csv


outputfile = open('woodname.csv','a',newline='')
OutputWriter = csv.writer(outputfile)


file = requests.get('http://www.wood-database.com/')
file.raise_for_status()

soupOb = bs4.BeautifulSoup(file.text,"lxml")

elems=soupOb.select('h3 a')

#print(elems[0])

for i in elems:
    OutputWriter.writerow(i.getText())
    
    
outputfile.close()

