# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:05:57 2026

@author: brand
"""

#Module 6 Problem 3

prince = 0
year = 0
interest = 0
total = 0

print("Input amount: ")
prince = int(input())
print("Input year to Maturity: ")
year = str(input())
if prince > 100000 and year == 5:
    interest = .6
    
elif prince > 50000 or prince == 100000 and year == 10:
    interest = .05

elif prince > 50000 or prince == 100000 and year == 5:
    interest = .04
else:
    interest = .02

amount = interest * prince

print("Principle amount: ",prince)
print()
print("Interest Rate: ",interest)
print()
print("Year 1 Interest: ",amount)