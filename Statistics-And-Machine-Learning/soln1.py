# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:46:44 2018

@author: Himol Shah
"""


import math

phy = [15,12,8,8,7,7,7,6,5,3]
his = [10,25,17,11,13,17,20,13,9,15]

n = len(phy)

xy = sum([h*k for (h,k) in zip(phy,his)])
x = sum(phy)
y = sum(his)
xx = sum([h*k for (h,k) in zip(phy,phy)])
yy = sum([h*k for (h,k) in zip(his,his)])

r = (n*xy - x*y)/math.sqrt(((n*xx - x**2)*(n*yy - y**2)))

ans = r

print("%.3f" % ans)
