# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 20:03:16 2018
Compress the String!
@author: Himol Shah
"""

from itertools import groupby

x = input()
a = []

for k, d in groupby(x):
    a.append(((len(list(d))), int(k)))
    
print(*a)
