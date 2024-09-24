# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:17:03 2024

@author: Asus
"""

# Nhập vào ba số nguyên dương
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

#kiểm tra điều kiện lặp thành tam giác
if a + b > c and a + c > b and b + c > a:
 #kiểm tra loại tam giac
 if a == b == c:
    print("Tam giác là: tam giác đều")
 elif a == b or b == c or a == c:
    print("Tam giác là: tam giác cân")
 elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Tam giác là: tam giác vuông") 
 else:
    print("Tam giác là: tam giác thường")
else:
    print("không hợp lệ!")
       