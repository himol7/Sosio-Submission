# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 22:12:40 2018
No Idea!
@author: Himol Shah
"""

n, m = [int(x) for x in input().split()]

arr = input().split()

a = set(input().split())
b = set(input().split())
print(sum([(i in a) - (i in b) for i in arr]))