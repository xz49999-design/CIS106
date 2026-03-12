# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:10:08 2026

@author: brand
"""

#Module 6 Problem 1

price = 0
quantity = 0

print("Enter quantity:")
quantity = int(input())


if quantity > 10000:
    price = 10    
else:
    if quantity > 5000:
        price = 20
    else:
        price = 30
        
extended = price * quantity
tax = extended * 0.7
extended_tax = extended + tax

print("Price per quantity: ", price)
print("Price before Taxes: ", extended)
print("Tax: ", tax)
print("Extended Price: ", extended_tax)
