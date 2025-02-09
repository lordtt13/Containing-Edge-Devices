# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:55:51 2019

@author: tanma
"""

# data = pd.read_csv("data.csv",header = None)

def threshold(arr,mean_arr,n):
    """
    

    Parameters
    ----------
    arr : data series, can be list, dataframe series
          Array you want to find the threshold on.
    mean_arr : float
        mean of the series
    n : float (between 0. and 1.)
        tolerance value, how much of the array should be included within

    Returns
    -------
    thresholds : float
        min and max value of included array inside tolerance array

    """
    j = 0.01
    excess = []
    while(len(excess) < n*len(arr)):
        excess = [i for i in arr if(i > mean_arr - j*mean_arr and i < mean_arr + j*mean_arr)]
        j += 0.01
    return min(excess),max(excess)

"""
min_val_one , max_val_one = threshold(data.iloc[:,1], data.iloc[:,1].mean(), 0.75)
min_val_two , max_val_two = threshold(data.iloc[:,1], data.iloc[:,2].mean(), 0.75)

data["Threshold on one"] = data.iloc[:,1].apply(lambda x:1 if (x<=max_val_one and x>=min_val_one) else 0)
data["Threshold on two"] = data.iloc[:,1].apply(lambda x:1 if (x<=max_val_two and x>=min_val_two) else 0)


plt.plot(data.iloc[:,1])
plt.savefig('foo.jpeg')
plt.close()
plt.plot(data.iloc[:,2])
plt.savefig('bar.jpeg')
plt.close()

data.to_csv("data_new.csv")
"""
