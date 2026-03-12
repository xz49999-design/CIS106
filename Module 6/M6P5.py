# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:11:04 2026

@author: brand
"""

# Module 6 Problem 5
name = str(0)
salary = 0
rank = 0
bonus = 0
total = 0

print("Please input last name: ")
name = str(input())

print("Please input salary: ")
salary = int(input())

print("Please input rank: ")
rank = int(input())

if rank > 10:
    bonus = 0.25
elif rank >= 5 or rank == 9:
    bonus = 0.2
else:
    bonus = 0.1
    
total = salary + (salary * bonus)
    
print("Employee last name: ",name)
print()
print("Total with bonus: ",total)