# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:55:51 2019

@author: tanma
"""
import pandas as pd


data = pd.read_csv("data.csv")

def threshold(arr,mean_arr,n):
    j = 0.01
    excess = []
    while(len(excess) < n*len(arr)):
        excess = [i for i in arr if(i > mean_arr - j*mean_arr and i < mean_arr + j*mean_arr)]
        j += 0.01
    return min(excess),max(excess)

min_val , max_val = threshold(data["23.0"], data["23.0"].mean(), 0.75)
min_val , max_val = threshold(data["64.0"], data["64.0"].mean(), 0.75)