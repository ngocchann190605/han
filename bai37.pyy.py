# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:15:10 2024

@author: Asus
"""
#bai37
# Nhập vào số nguyên dương n
n = int(input("Nhập số chẵn lớn hơn 0: "))

# Kiểm tra điều kiện n phải là số chẵn và lớn hơn 0
while n <= 0 or n % 2 != 0:
    n= int(input("Không hợp lệ.vui lòng nhập lại"))
# Tính tổng S
S = sum(range(2, n + 1, 2))
print("Tổng S =", S)