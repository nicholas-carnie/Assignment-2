#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:15:07 2023

@author: carnie
"""

# Convert the following for loops into the equivalent while loop: 
    
# a)    for i in range (1,10):
#           print (i,i*i)
       
# Run the program. Include a screenshot of the output on the screen in your zip file.

number = 1                              #Assign the variable: Integer '1' into variable 'number'

while number > 0 and number < 10:       #Initialize while loop. Continues loop for as long as variable 'number' is > 0 and 'number' < 10
    multiplication = number * number    #Body of for loop. multiplication = int(number) * int(number). Converts 'multiplication' to integer.
    print(number, multiplication)       #Calls print function for variables 'number' & 'multiplication'
    number = number + 1                 #Sets new value for variable "number" as "number + integer 1"
 