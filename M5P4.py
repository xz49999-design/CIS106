# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 18:26:16 2026

@author: brand
"""
name = 0
warrentee = 0
cost = 0

print("What is the name of the appliance?")
name = str(input())

print("What is the cost of the Appliance?")
cost = float(input())
if cost > 1001:
    warrentee = 0.1
else:
    warrentee = 0.05

wart = cost * warrentee
total = wart + cost
print(name)
print("Cost: ",cost)
print("Warrentee amount: ",warrentee,"%")
print("Total: ", total)