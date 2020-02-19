# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:27:21 2020

@author: Tanmay Thakur
"""

import pandas as pd
from parametrizing import threshold


data = pd.read_csv('features.csv')

data = data.drop(['Date','Time'], axis = 1)

features = len(data.columns)
timestep = 60

def ax(data, timestep):
    for j in range(0, len(data), timestep):
        if (j > len(data) - timestep):
            yield(threshold(data[j:len(data)], data[j:len(data)].mean(), 0.75))
        else:
            yield(threshold(data[j:j+timestep], data[j:j+timestep].mean(), 0.75))

for i in data.columns:
    for j in range(len(data[i])//timestep + 1):                
        print(next(ax(data[i], timestep)))