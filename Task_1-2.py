#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:19:46 2023

@author: carnie
"""

#Write a python program that ask for an integer input from the user and prints its multiplications on the screen. 
#The program should follow these steps:
    
#Print on the screen, prompting for an input number from the user (e.g., ‘Enter an integer value’)
#Print the multiplication tables of a given number for 10 times
    
#An example of the program output when a user enters 5: 5x1=5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20 
#5 x 5 = 25 
#5 x 6 = 30 
#5 x 7 = 35 
#5 x 8 = 40 
#5 x 9 = 45 
#5 x 10 = 50

multiple = 2                                                #Assign the variable: Integer '2' into variable 'multiple'

integer = input("Enter an integer value:\n")                #Calls input function from user. Prints 'Enter an integer value' with an escape character 
integer = int(integer)                                      #Converts string 'integer' to integer 'integer' into variable 'integer'

for x in range(9):                                          #Intilize for loop with placeholder 'x' in range function. Range executes 9 times only.
    equation = integer * multiple                           #Body of for loop. Equation = int(integer) * int(multiple). Converts equation to integer.
    print("%s x %s = %s" %(integer, multiple, equation))    #Calls print function. Prints 'equation' formula with use of a tuple.
    multiple = multiple + 1                                 #Sets new value for variable 'multiple' as 'multiple + integer 1'

    