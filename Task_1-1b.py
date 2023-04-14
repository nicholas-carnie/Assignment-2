#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:47:40 2023

@author: carnie
"""

# • Print first 10 even numbers using for loop (e.g., 2, 4, 6, ...., 16, 18, 20)      

print("Welcome to Task 1(b) solution.\n")               #Calls print function with welcome message

print("\nPrint first 10 even numbers using for loop")   #Calls print function with purpose of program

for evenNumber in range(0, 21):         #Intilize for loop with placeholder 'evenNumber' in range function. Begins at integer 0 & ends at integer 21.
    if (evenNumber % 2 == 0):           #Body of for loop with nested if statement. Checks modulus of evenNumber to accept even numbers only
        print(evenNumber)               #Calls print function with placeholder 'evenNumber'. Executes each value in the range until exhausted.
