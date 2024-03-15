# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:44:16 2024

@author: san
"""

# n = int(input("Enter n :"))
# a = 0
# b = 1
# c = a + b
# print(a)
# print(b)
# while c <= n:
#     print(c)
#     a = b
#     b = c
#     c = a+b

n = int(input("Enter n :"))
f = 1
while n >= 1:
    f = f*n
    n = n-1
print("factorial", f)
    