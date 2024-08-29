# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:12:45 2024

@author: Student
"""

print("nhập thời gian")
a=int(input("giờ="))
b=int(input("phút="))
c=int(input("giây"))
if 0<=a<24 and 0<=b<=60 and 0<=c<=60:
    print(f"thời gian hợp lệ:{a}:{b}:{c}")
else:
    print("thời gian không hợp lệ")