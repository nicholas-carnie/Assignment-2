#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:15:07 2023

@author: carnie
"""

# Convert the following for loops into the equivalent while loop:
       
# b)    sum = 0
#       for i in range (10,0,-1):
#           sum = sum + i
#           print (i,sum)
    
# Run the program. Include a screenshot of the output on the screen in your zip file.
    

number = 10                             # Assign the variable: Integer '10' into variable 'number'
sum_num = 0                             # Assign the variable: Integer '0' into variable 'sum_number'

while number > 0 and number <= 10:      #Initialize while loop. Continues loop for as long as variable 'number' is > 0 and 'number' <= 10
    sum_num = sum_num + number          #Body of for loop. int(sum_num) = int(sum_num) + int(number).
    print(number, sum_num)              #Calls print function for variables 'number' & 'sum_num'
    number = number - 1                 #Sets new value for variable "number" as "number - integer 1"
    
    
    