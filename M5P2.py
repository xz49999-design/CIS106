# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 17:56:14 2026

@author: brand
"""

#M5P2
item = 0
print("Pick item A or B")
item = str(input())
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00
    
print("How many of the item?:")
quantity = int(input())

total = quantity * unit_price

print("Your total is: ",total)