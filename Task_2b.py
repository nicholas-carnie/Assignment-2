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
    
print("Welcome to Task 2(b) solution.\n")                                   #Calls print function - Welcome message

print("\nConvert the following for loop into the equivalent while loop")    #Calls print function - Purpose of program
    
print("\nFor loop")                                                         #Calls print function - For Loop section

#For Loop to be converted to check same

sum = 0
for i in range (10,0,-1):
    sum = sum + i
    print (i,sum)



print("\nWhile loop equivalent")        #Calls print function - For Loop equivalent

number = 10                             # Assign the variable: Integer '10' into variable 'number'
sum = 0                                 # Assign the variable: Integer '0' into variable 'sum_number'

while number > 0:                                       #Initialize while loop. Continues loop for as long as variable 'number' is > 0
    print("%s + %s = %s" %(number, sum, sum + number))  #Print function with each loop iteration. Details formula taken from a tuple. Readability increased from 'for loop' example
    sum += number                                       #Sets new value for variable "sum" as "sum + number"
    number -= 1                                         #Sets new value for variable "number" as "number - integer 1"
    
