# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:07:12 2024

@author: Student
"""

print("nhập vào 4 số nguyên")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
d=float(input("d="))
sonhonhat=a
if b<a:
    sonhonhat=b
if c<a:
    sonhonhat=c
if d<a:
    sonhonhat=d
print("số nhỏ nhất trong 4 số là:",sonhonhat)