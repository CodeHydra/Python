# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 09:39:21 2019

@author: Melroy Pereira
"""

n=int(input("enter the no.of rows"))
for i in range(n):
    for j in range(i):
        print("#",end="")
        j=j+1
    i=i+1
    print()