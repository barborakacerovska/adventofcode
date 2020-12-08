# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:46:09 2020
@author: Baru
"""

import numpy as np

input = np.loadtxt('input.txt')

''' DAY 1a
I am going to substract the field from 2020 and then compare it with 
the input'''
common = np.intersect1d(input,2020-input)
answer = np.prod(common)
print(answer)

''' DAY 1b 
First, I substract the input from 2020 which gives me an array where one 
of the numbers is a sum of two numbers from input. Second, if the sum is bigger 
than any of the numbers in the input, I delete it.  '''


subs = 2020-input
for s in subs:
    for i in input:
        if s>i and (s-i) in input:
            index = np.where(subs == s)
            answer = np.prod(np.array([i,s-i,input[index]]))
            break
    else:
        continue
    break
print(answer)


