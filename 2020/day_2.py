# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:49:38 2020

@author: Barunka
"""

import numpy as np

password=np.loadtxt("static/input_day2.txt", dtype=str, delimiter=':')



"""
Part one
"""

letter = np.array(list(map(lambda x: x.split(' '), password[:,0])))
number = np.array(list(map(lambda x: x.split('-'), letter[:,0])))
matice = (np.vstack((number[:,0],number[:,1],letter[:,1], password[:,1]))).T

correct = 0
incorrect = 0

#for i in matice:
#    if  int(i[0]) <= i[3].count(i[2]) <= int(i[1]):
#        correct+=1
#    else:
#        incorrect+=1
#
#print('incorrect = ',incorrect )
#print('correct = ',correct )


"""
Part two
"""
for i in matice:
    if (i[3][int(i[0])] == i[2]) ^ (i[3][int(i[1])] == i[2]):
       correct+=1
    else:
       incorrect+=1

print('incorrect = ',incorrect )
print('correct = ',correct )