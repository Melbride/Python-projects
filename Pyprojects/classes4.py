# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 00:20:14 2024

@author: san
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

# Creating instances of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

# Accessing attributes and calling methods
print(dog1.name)    # Output: Buddy
print(dog1.age)     # Output: 5

print(dog2.name)    # Output: Max
print(dog2.age)     # Output: 3

dog1.bark()         # Output: Buddy says woof!
dog2.bark()         # Output: Max says woof!
