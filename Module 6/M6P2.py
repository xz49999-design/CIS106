# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:48:59 2026

@author: brand
"""

# Module 6 Problem 2

quantity = 0
unit_cost = 0
part = 0
total = 0

print("Enter your part #: ")
part = str(input())



if part == ("10") or part == ("55"):
    unit_cost = 1
elif part == ("99"):
        unit_cost = 2
elif part == "80" or part == "70":
    unit_cost = 3
else:
    unit_cost = 5
            

print("Quantity of Item: ")
quantity = int(input())


total = quantity * unit_cost

print("Item Number: ",part)
print("Price per unit: ",unit_cost)
print("Quantity: ",quantity)
print("Total cost: $", total)