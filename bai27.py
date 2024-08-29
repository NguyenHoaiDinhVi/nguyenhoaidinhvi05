# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:45:11 2024

@author: Student
"""

#chuvi và diện tích hình chữ nhật:
print("tính chu vi và diện tích hình chữ nhật")
a=float(input("chiều dài="))
b=float(input("chiều rộng="))
cv=2*(a+b)
dt=a*b
print("diện tích hình chữ nhật=",round(dt,2))
print("chu vi hình chữ nhật=",round(cv,2))    
#chu vi và diện tích hình vuông:
print("nhập cạnh của hình vuông:")
a=float(input("cạnh="))
cv=a*4
dt=a*a
print("diện tích hình vuông=",round(dt,2))
print("chu vi hình vuông=",round(cv,2))   
#chu vi và diện tích hình tròn:
print("nhập bán kính của hình tròn:")
a=float(input("bán kính="))
cv=2*a*3.14
dt=a*a*3.14
print("diện tích hình tròn=",round(dt,2))
print("chu vi hình tròn=",round(cv,2)) 