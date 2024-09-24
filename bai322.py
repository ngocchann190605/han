# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:38:37 2024

@author: Asus
"""

# Nhập vào số km đã đi
km = float(input("Nhập số km đã đi: "))

# Tính tiền cước taxi
if km == 1:
    tongtien = 15000
elif  1 < km <= 5: #elif  1 < km <= 5:
    tongtien = 15000 + (km - 1) * 13500
else:
    tongtien= 15000 + (5 - 1) * 13500 + (km - 5) * 11000

# Giảm giá nếu đi hơn 120 km
if km > 120:
    tongtien *= 0.9
print(f"Tổng tiền cước taxi (km) là: {tongtien:.0f} đ")