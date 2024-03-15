# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:05:01 2024

@author: san
"""
# this pointer

class Employee:
    'an example of how to create a class'
    empcount=0
   
    def _init_(self,n,s):
       self.empname=n
       self.empsal=s
       Employee.empcount+=1
       return
    def displayemp(self):
       print("My name is ", self.empname)
       return
P= Employee("James",7000)
q= Employee("James",7000)
k= Employee("James",7000)
p.displayemp()
# print(k.empcount)
hasttr(k,"empsal")
setattr(k,"empsal",90000)
k.empsal
setattr(k, "allowance", 8000)
k.allowance  
      