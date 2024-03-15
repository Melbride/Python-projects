# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 12:02:57 2024

@author: san
"""
principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input("Enter the principle amount:"))
    if principle <=0:
        print("Principle cant be less than or equal to zero")
while rate <= 0:
    rate = float(input("Enter the rate interest:"))
    if rate <=0:
        print("Rate cant be less than or equal to zero")
while time <= 0:
    time = int(input("Enter the time in years:"))
    if time <=0:
        print("Time cant be less than or equal to zero")

total = principle * (1+rate/100)
print(principle)
print(rate)
print(time)