# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 19:07:21 2026

@author: brand
"""

print("insert last name:")
name = str(input())
print("insert number of dependents:")
depend = int(input())
print("insert gross:")
gross = int(input())

adjust = gross - (depend * 12000)

if gross > 50001:
    tax = .2
else:
    tax = .1

total_tax = adjust * tax
if total_tax < 0:
    total_tax + 100
total = total_tax + adjust

print(name)
print("Gross Income:", gross)
print("Dependents: ",depend)
print("Income Tax: ",tax)
print("Adjusted: ",total)