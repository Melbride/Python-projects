
"""
Created on Thu Mar 14 14:18:07 2024

@author: san
"""

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if(b==0):
        return "Cannot divide by zero"
    else:
        return a / b
    
    
choice = input("Enter choice (1,2,3,4): ")
# the choice stands for the functions above respectively
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if(choice== "1"):
    print(addition(num1, num2))
    
elif(choice== "2"):
    print(subtraction(num1, num2))
    
elif(choice== "3"):
    print(multiplication(num1, num2))
    
elif(choice== "4"):
    print(division(num1, num2))
else:
    print("Invalid input!")
    
    
    
    
    
    
    
    
    
    
    
