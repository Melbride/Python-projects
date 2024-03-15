# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:34:30 2024

@author: san
"""

# import sys
# list=[1,2,3,4]
# it = iter(list) # this builds an iterator object
# print (next(it)) #prints next available element in iterator
# # Iterator object can be traversed using regular for statement
# # !usr/bin/python3
# for x in it:
#     print (x, end=" ")
# # or using next() function
#     while True:
#         try:
#             print (next(it))
#         except StopIteration:
#             sys.exit()
            
    # generator
   
# import sys
# def fibonacci(n): #generator function
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(5) #f is iterator object
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit() 
 
 
 # generator
import   sys
def squares(n): #generator function
    counter = 0
    while True:
        if (counter > n):
            return
        yield counter**2
        counter += 1
sqr = squares(5) #sqr is iterator object
while True:
    try:
        print (next(sqr))
    except StopIteration:
            sys.exit()