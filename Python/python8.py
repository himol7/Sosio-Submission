# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 00:13:08 2018
ginortS
@author: Himol Shah
"""

s = input()
s = sorted(s, key = lambda x : (x.isdigit() and int(x)%2==0, x.isdigit(), x.isupper(), x.islower(), x))
print(*(s), sep = '')

