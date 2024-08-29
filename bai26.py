# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:50:55 2024

@author: Student
"""

a = float(input("Nhập số a= "))
b = float(input("Nhập số b= "))
c = float(input("Nhập số c= "))
if a > b:
    a, b = b, a  
if b > c:
    b, c = c, b  
if a > b:
    a, b = b, a   
print(f"Ba số theo thứ tự tăng dần là: {a}, {b}, {c}")