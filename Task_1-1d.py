#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:48:56 2023

@author: carnie
"""

# • Print sum of first 10 numbers using for loop
# (e.g., print the sum of 1+ 2 + 3 + ... + 8 + 9 + 10).

print("Welcome to Task 1(d) solution.\n")                   #Calls print function with welcome message

print("Print sum of first 10 numbers using for loop\n")     #Calls print function with purpose of program

sum = 0                     #Assigns '0' into sum function

for x in range(1,11):       #Intilize for loop with placeholder 'x' in range function. Begins at integer 1 & ends at integer 11.
     sum += x               #Body of for loop. Executes sum function with placeholder 'x'. Sum = Sum + 1. As the range didn't specify the increment, it automatically assigns integer '1'
     print(sum)             #Print function to display sum of the numbers at each loop iteration.

print("\nThe sum of the numbers from 1 to 10 is",sum) #Print function is called when for loop is exhausted. The loop has passed 10 times to give a final value for sum = 55.
    
    
