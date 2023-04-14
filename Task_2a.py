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


print("Welcome to Task 2(a) solution.\n")                                   #Calls print function - Welcome message

print("\nConvert the following for loop into the equivalent while loop")    #Calls print function - Purpose of program
    
print("\nFor loop")                             #Calls print function - For loop section
for i in range(1, 10):                          #For loop example
    print("{} x {} = {}".format(i,i, i*i))      #For loop example


print("\nWhile loop equivalent")                #Calls print function - While loop equivalent
i = 1                                           #Sets interger 1 into variable i
while i < 10:                                   #Initiates while loop with condition i less than 10
    print("{} x {} = {}".format(i, i, i*i))     #Calls print function - Equation & result
    i+=1                                        #Sets new value for variable "i" as "i + integer i"
