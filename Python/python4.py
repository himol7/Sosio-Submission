# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 22:58:58 2018
Words Score
@author: Himol Shah
"""

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    
    total = 0
    
    for word in words:
        score = 0
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score = score + 2
        else:
            score = score + 1
        
        total = total + score

    return total


n = int(input())
words = input().split()
print(score_words(words))