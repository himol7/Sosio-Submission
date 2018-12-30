# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 23:24:32 2018
Default Arguments
@author: Himol Shah
"""

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())

        
