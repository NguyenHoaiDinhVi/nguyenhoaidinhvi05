# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:08:45 2024

@author: Student
"""

print("nhập vào 3 số")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a>b>c:
    print("số lớn nhất là:",a)
elif a>c>b:
    print("số lớn nhất là:",a)
elif b>a>c:
    print("số lớn nhất là:",b)
elif b>c>a:
    print("số lớn nhất là:",b)
elif c>a>b:
    print("số lớn nhất là:",c)
else:
    print("số lớn nhất là:",c)