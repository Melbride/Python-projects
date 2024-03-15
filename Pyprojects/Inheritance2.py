# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 00:29:03 2024

@author: san
"""

class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Creating instances of the derived classes
dog = Dog("Canine")
cat = Cat("Feline")

# Calling the speak method of each instance
dog.speak()   # Output: Woof!
cat.speak()   # Output: Meow!
