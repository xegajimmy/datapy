# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:30:19 2016

@author: jimmy
"""

import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import time

Location = r'd:\Python35\mems.csv'
df = pd.read_csv(Location)  #delimiter=';'

df.head()
df.tail()
df.pop('dummy1')         #del df['dummy1']
df.pop('dummy2')        #del df['dummy2']
idlist=list(df['dev_id'].unique())
if len(idlist)==1:
    id=str(idlist[0])
    del df['dev_id']
'''
date=str(df.collect_data.unique())
a=time.strptime(date[2:10], '%Y/%m/%d')
secs=time.mktime(a)
'''

df['collect_asctime']=df.collect_data.apply(lambda x:x[0:9])+df.collect_time
#df.assign(collect_asctime = lambda x:(x['collect_data'][0:9]+x['collect_time']))
'''
a=time.strptime(df['collect_asctime'][0], '%Y/%m/%d %X')
secs=time.mktime(a)
'''
df['struct_ts']=df.collect_asctime.apply(lambda x:time.strptime(x,'%Y/%m/%d %X'))
df['stampts']=df.struct_ts.apply(lambda x:time.mktime(x))
df['stamptime']=df.stampts+df.collect_ms/1000
del df.collect_asctime

del df['collect_asctime']


