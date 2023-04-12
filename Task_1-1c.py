#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:48:22 2023

@author: carnie
"""

# • Print first 10 odd numbers using while loop (e.g., 1, 3, 5, ..., 15, 17, 19)

x = 1                   #Assign the variable: Integer '1' into variable 'x'

while x < 20:           #Initialize while loop. Continues loop for as long as variable 'x' is < 20
    if x % 2 == 1:      #Initialize nested if statement with condition: variable 'x' modulus of integer 2 = 1
        print(x)        #Body of if statement when true. Calls print function for variable 'x'
    x = x + 1           #Sets new value for variable 'x' as 'x + integer 1'
