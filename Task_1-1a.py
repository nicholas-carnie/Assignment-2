#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:44:33 2023

@author: carnie
"""

# • Print first 10 numbers using while loop (e.g., 1, 2, 3, ...., 8, 9, 10)

print("Welcome to Task 1(a) solution.\n")               #Calls print function with welcome message

print("\nPrint first 10 numbers using while loop")      #Calls print function with purpose of program

x = 1                       #Assign the variable: Integer '1' into variable 'x'

while x <= 10:              #Initialize while loop. Continues loop for as long as variable 'x' is > 0 and 'x' < 11
    print(x)                #Body of while loop. Calls print function for variable 'x'
    x += 1                  #Sets new value for variable 'x' as 'x + integer 1'
    
