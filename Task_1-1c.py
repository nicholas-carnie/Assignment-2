#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:48:22 2023

@author: carnie
"""

# • Print first 10 odd numbers using while loop (e.g., 1, 3, 5, ..., 15, 17, 19)

print("Welcome to Task 1(c) solution.\n")               #Calls print function with welcome message

print("\nPrint first 10 odd numbers using while loop")  #Calls print function with purpose of program

x = 1                   #Assign the variable: Integer '1' into variable 'x'

while x < 20:           #Initialize while loop. Continues loop for as long as variable 'x' is < 20
    if x % 2 != 0:      #Initialize nested if statement with condition: variable 'x' modulus of integer 2 != 0 to check odd number.
        print(x)        #Body of if statement when true. Calls print function for variable 'x'
    x += 1              #Sets new value for variable 'x' as 'x + integer 1'
