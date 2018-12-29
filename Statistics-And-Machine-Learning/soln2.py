# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 23:16:46 2018

@author: Himol Shah
"""

phy = [15,12,8,8,7,7,7,6,5,3]
his = [10,25,17,11,13,17,20,13,9,15]

n = len(phy)

xy = sum([h*k for (h,k) in zip(phy,his)])
x = sum(phy)
y = sum(his)
xx = sum([h*k for (h,k) in zip(phy,phy)])

a = (n*xy - x*y)/(n*xx - x**2)
b = (y*xx - x*xy)/(n*xx - x**2)

ans = a

print("%.3f" % ans)
