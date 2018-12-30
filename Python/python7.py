# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 00:11:33 2018
Athelete Sort
@author: Himol Shah
"""

n, m = map(int, input().split())
arr = [input() for _ in range(N)]
k = int(input())

for row in sorted(arr, key=lambda row: int(row.split()[k])):
    print(row)