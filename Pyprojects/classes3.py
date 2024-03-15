# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:05:13 2024

@author: san
"""
class Robot:
    def __init__(self, name, colour, weight):
        self.name = name
        self.colour = colour
        self.weight = weight
# creating two instances of the Robot class
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

print("Here is the first robot characteristics")

print("My name is " +  r1.name)
# accessing attributes of r1 and r2 instances
print(r1.colour)
print(r1.weight)

print("\n")
print("Here is the second robot characteristics")
print("\n")
# used an f string to print the r2 name
print(f"My name is {r2.name}" )
print(r2.colour)
print(r2.weight)




