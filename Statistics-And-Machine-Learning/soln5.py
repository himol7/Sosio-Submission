# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 23:36:17 2018

@author: Himol Shah
"""

'''

4x - 5y + 33 = 0 (line of y on x)
byonx = 4/5

20x - 9y - 107 = 0 (line of x on y)
bxony = 9/20
'''
import math
# variance of y when sigx = 3

sigx = 3
byonx = 4/5
bxony = 9/20

r = math.sqrt(byonx*bxony)
'''
byonx = r*(sigy/sigx)
'''

sigy = (byonx*sigx)/r

ans = sigy**2

print(ans)
