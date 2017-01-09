#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:22:52 2017

@author: jimmyMac
"""

height=1.79
weight=68.7
bmi=weight/height**2
print(bmi)

type(bmi)   #float
x="body mass index"
type(x)    #str

fam=[1.73,1.68,1.71,1.89]
type(fam)

#list 方法
fam[1]
fam[-1]
#slice
fam[1:3]
#add
famext=fam+['a','b']    #[1.73, 1.68, 1.71, 1.89, 'a', 'b']
#del
del(famext[4])  #[1.73, 1.68, 1.71, 1.89, 'b']
#change
famext[3]='d'   #[1.73, 1.68, 1.71, 'd', 'b']

y=famext
y[2]='a'
famext

x=list(famext)
x[2]='x'
famext  #[1.73, 1.68, 'a', 'd', 'b']
x       #1.73, 1.68, 'x', 'd', 'b']

#function
tallest=max(fam)
round(1.68,1)
help(round)

#method
fam.index(1.68)
fam.count(1.68)
fam.append('me')    #[1.73, 1.68, 1.71, 1.89, 'me']
dir(fam)

import numpy as np

from numpy import array
array([1,2,3])      #array([1, 2, 3])