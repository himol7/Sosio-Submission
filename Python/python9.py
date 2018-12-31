# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 09:29:27 2018
Triangle Quest 2
@author: Himol Shah
"""
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave 
    print(((10**i-1)//9)**2)