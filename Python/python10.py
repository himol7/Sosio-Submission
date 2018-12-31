# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 09:46:00 2018
Triangle Quest
@author: Himol Shah
"""

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(i*(( 10**i - 1 )/9)))