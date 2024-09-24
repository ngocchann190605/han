# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:07:30 2024

@author: Asus
"""

# Nhập giá trị n
n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra điều kiện n phải lớn hơn 0
if n <= 0:
    print("không hợp lệ!")

# Tính tổng S
tong = sum(i**2 for i in range(1, n + 1))
print("Tổng S =", tong)
