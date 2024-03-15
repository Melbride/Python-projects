# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:38:32 2024

@author: san
"""

# def sayhi():
#     print("hello world")
#     return
# sayhi()


# def sayhix(k,nam):
#     print("hello",nam)
#     return
# sayhix(5,"melbride")


# def sayhix(k,nam):
#     for i in range (k):
#         print("Hello",nam)
#     return
# sayhix(5,"jane")


# def addtwo(x,y):
#     'A function that adds two numbers'
#     total=x+y
#     return total
# print(addtwo(5,6))
    

# temps=[7,8]
# def addtwo(nums):
#     'A function that add two numbers'
#     nums[0]*=5
#     nums[1]*=2
#     total=nums[0]+ nums[1]
#     return total
# print(addtwo(temps))
# print(temps)
 

a,b=7,"jane"
def sayhi(k,nam):
    'A function to say hi to nam k times'
    for i in range (k):
        print("Hello", nam)
    return
sayhi(a,b)


addtwo= lambda a,b:a+b
print(addtwo(6,7))


sayhi=lambda nam: print("Hello",nam)
areac=lambda r: 3.142*r*r
print(areac(2))
