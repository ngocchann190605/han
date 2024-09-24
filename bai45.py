# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:15:08 2024

@author: Asus
"""

s=0
ts = 0
ms = 1
n = int(input("Nhap n: "))
while n <= 0:
    n = int(input("Nhap n: "))
x = float(input("Nhap x: "))
for i in range(1, n+1):
    ts = x**i
    ms = ms + i
    s += ts/ms
print(s)
