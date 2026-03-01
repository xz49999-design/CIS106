# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 18:13:16 2026

@author: brand
"""

print("Enter amount of books to order: ")
amount = float(input())

print("Enter cost per book: ")
cost = float(input())

total = cost * amount
extra = 0
tax = total + extra

if total > 50.00:
    extra = 0
    print("Your total is:", total)
    print("Shipping Tax:", extra)
    print("Your total with shipping is: ",tax)
else:
    extra = 25.00
    print("Your total is:", total)
    print("Shipping Tax:", extra)
    print("Your total with shipping is: ",tax)