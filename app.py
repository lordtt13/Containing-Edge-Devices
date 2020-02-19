# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:35:59 2020

@author: Tanmay Thakur
"""
import pickle
import numpy as np

from parametrizing import threshold


timestep = 60

def append_new(data, point):
    data.append(point)
    return data.pop(0)


for _ in range(timestep):
    # dict_new = function_call()
    data_temp, data_humid = pickle.load(open( "data_temp.pickle", "rb" )), pickle.load(open( "data_humid.pickle", "rb" ))
    for key, value in dict_new.items():
        if(key == "Temperature"):
            append_new(data_temp, value)
            pickle_out = open("data_temp.pickle","wb")
            pickle.dump(data_temp, pickle_out)
            pickle_out.close()
            print(threshold(data_temp, np.mean(data_temp), 0.75))
        else:
            append_new(data_humid, value)
            pickle_out = open("data_humid.pickle","wb")
            pickle.dump(data_humid, pickle_out)
            pickle_out.close()
            print(threshold(data_humid, np.mean(data_humid), 0.75))