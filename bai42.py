# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:26:26 2024

@author: Asus
"""
#bai 42
s=0
n = int(input("nhap n: "))
while n <=0:
    n = int(input("nhap n: "))
    
for i in range(1, n+1):
    s+= 1/ i* (i+1)
print(round(s,2))