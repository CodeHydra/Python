# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 10:22:30 2019

@author: Melroy Pereira
"""

def add_subt(x,y):
    c=x+y
    d=x-y
    return c,d
x=int(input("enter the value of x"))
y=int(input("enter the value of y"))

answer1,answer2=add_subt(x,y)
print(answer1,answer2)