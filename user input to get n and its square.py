# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 07:55:19 2019

@author: Melroy Pereira
"""

####### Taking user input to print n&n^2

n=int(input("enter the value"))
for i in range(1,n):
    k=i
    j=i*i
    print([k , j],end="")
    i=i+1