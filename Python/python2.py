# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 20:22:10 2018
Iterables and Iterators
@author: Himol Shah
"""
from itertools import combinations

n = int(input())
l = input().split()
k = int(input())

comb = list(combinations(l, k))
lists = filter(lambda x: 'a' in x, comb)
print("%.3f" % (len(list(lists))/len(comb)))