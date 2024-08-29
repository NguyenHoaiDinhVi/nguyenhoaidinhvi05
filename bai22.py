# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:19:16 2024

@author: Student
"""

print("giải phương trình bậc nhất ax+b=0")
a=float(input("nhập giá trị của a:"))
b=float(input("nhập giá trị của b:"))
if a==0 and b==0:
    print("phương trình có vô số nghiệm")
elif a==0 and b!=0:
    print("phương trình vô nghiệm")
elif a!=0:
    print("phương trình có nghiệm x=",-b/a)
else:
    print("không xác định được")