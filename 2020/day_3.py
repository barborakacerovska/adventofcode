1# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:09:12 2020
@author: Baru
"""


import numpy as np
import functools 

""" Part One
First I need to load the input. The issue here is that it reads hash symbol
as a comment. I need to define, that there are no comments. """

road=np.loadtxt("static/input_day3.txt", dtype=str, comments=None)
trees=0

for i in np.arange(road.shape[0]):
    n=(i*3)%len(road[1]) #řádky se opakují, vždycky vezmu zbytek
    if road[i][n]== '#':
        trees+=1
    
print('Part One: There are {} trees.'.format(trees))



"""Part two"""
slopes = (1,1),(3,1),(5,1),(7,1),(1,2)
trees=np.zeros(len(slopes))

for m,slope in enumerate(slopes):
    right=slope[0]
    down=slope[1]
    
    for i in np.arange(road.shape[0]):
        n=(i*right)%len(road[1]) #řádky se opakují, vždycky vezmu zbytek
        if i*down > road.shape[0]:
            break
        elif road[i*down][n]== '#':
            trees[m]+=1
        else:
            continue
result=functools.reduce(lambda a,b : a*b,trees)
print('Part Two: There are {} trees.'.format(result))