# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 09:42:48 2019

@author: Melroy Pereira
"""

n=int(input("enter the no.of rows"))
for i in range(n):
    for j in range(n-i):
        print("#",end="")
        j+=1
    i+=1
    print()