#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:07:48 2017

@author: jimmyMac
"""

import numpy as np

height=[1.73, 1.68, 1.71, 1.89, 1.79]
weight=[65.4, 59.2, 63.6, 88.4, 68.7]

np_height=np.array(height)
np_weight=np.array(weight)

bmi=np_weight/np_height**2
bmi
bmi>23
#array([False, False, False,  True, False], dtype=bool)
bmi[bmi>23]
#array([ 24.7473475])
type(bmi)   #numpy.ndarray

np_2d=np.array([height,weight])
#array([[  1.73,   1.68,   1.71,   1.89,   1.79],
#       [ 65.4 ,  59.2 ,  63.6 ,  88.4 ,  68.7 ]])
np_2d.shape         #(2, 5)
np_2d[0]
np_2d[0][2]

#random
height=np.round(np.random.normal(1.75,0.2,5000),2)
weight=np.round(np.random.normal(60.32,15,5000),1)

np_city=np.column_stack((height,weight))

np_city.mean(axis=0)
np.median(np_city[:,0])
np.median(np_city,axis=0)
np.corrcoef(np_city[:,0],np_city[:,1])
np.std(np_city,axis=0)  #array([  0.20212516,  14.90820588])