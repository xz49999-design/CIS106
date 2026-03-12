# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:02:19 2026

@author: brand
"""

# Module 6 Problem 4

quantity = 0
price = int(0)
total = 0

print("Input quantity of tickets: ")
quantity = int(input())

if quantity >= 25:
    price = 50
elif quantity == 10 or quantity >= 10 or quantity == 24:
    price = 60
elif quantity == 5 or quantity >=5 or quantity == 10:
    price = 75
else:
    price = 75

total = quantity * price

print("Amount of tickets: ", quantity)
print("Price per tickets: ",price)
print("Total cost: ", total)