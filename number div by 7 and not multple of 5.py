# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 14:18:37 2019

@author: Melroy Pereira
"""

x=int(input("enter the first value"))
y=int(input("enter the second value"))
i=x
while(i<=y):  
    if(i%7==0 & i%5==0):
        print(i)
    i+=1