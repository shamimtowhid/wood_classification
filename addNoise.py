#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 23:14:41 2017

@author: shamim
"""

import numpy as np

def synthesize(im, r, c):
    gaussian_noise = np.random.normal(0.0,0.6,(r,c,3))
    gaussian_noise = 0.5 * gaussian_noise
    noise_added = im + gaussian_noise
    return noise_added
  