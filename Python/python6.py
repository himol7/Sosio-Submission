# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 23:39:44 2018
Reduce Function
@author: Himol Shah
"""

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator