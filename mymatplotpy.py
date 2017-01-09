#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:43:52 2017

@author: jimmyMac
"""

import matplotlib.pyplot as plt
import numpy as np

year=[1950,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]
pop=[1.0,1.262,1.650]+pop
year=[1800,1850,1900]+year

#plt.plot(year,pop)
plt.fill_between(year,pop,0,color='green')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks(range(0,12,2))

plt.show()
#散点图
plt.scatter(year,pop)
plt.show()

values=np.random.normal(3,4,5000)
#直方图
plt.hist(values,bins=30)
plt.show()