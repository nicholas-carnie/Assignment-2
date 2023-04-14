#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 10:19:06 2023

@author: carnie
"""

# Task 3: Interpretation of loop codes

print("Welcome to Task 3(b) solution.\n")        #Calls print function - Welcome message

i = 1           #Assign the variable: Integer '1' into variable 'i'

while i < 3:    #Initialize the while/else loop. Continues loop for as long as variable "i" is less than integer 3
    print(i)    #Body of while loop. Calls print function for variable "i"
    i = i + 1   #Sets new value for variable "i" as "i + integer 1"
else:           #else block initilizes when while loop is exhausted. ie i >= 3
    print(0)    #calls print function for integer "0"
    
#The expected output for this while loop is:
    #   1
    #   2
    #   0
