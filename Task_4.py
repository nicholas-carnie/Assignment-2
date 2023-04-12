#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:13:25 2023

@author: carnie
"""

#You are hired as a software coder for Movies4Us Pty Ltd located in Melbourne, Australia. Your task is
#to develop a software program that issues 200 movie tickets. Your software program is to print
#“welcome to Movie4Us” to the first 200 users but write “there is no more ticket” to the 201th user.
#The software also needs to display how many tickets are available to each customer.
#For example, if Tim is 50th user to buy the movie ticket, your software program should display “You
#are the 50th user. The number of remaining tickets is now 150”. Prepare software code with
#sufficient comments to explain the progress.


tickets_issued = 0                                      #Assign the variable: Integer '0' into variable 'tickets_issued'
tickets_remaining = 200                                 #Assign the variable: Integer '200' into variable 'tickets_remaining'

while tickets_issued >= 0 and tickets_issued <= 200:    #Initialize while loop. Continues loop for as long as variable 'tickets_issued' is >= 0 and 'tickets_issued' <= 200
    tickets_issued = tickets_issued + 1                 #Body of while loop. Formula: Increments tickets_issued by 1 for every pass of loop
    tickets_remaining = tickets_remaining - 1           #Decrements tickets_remaining for every pass of the loop
    print("Welcome to Movie4Us")                        #Calls print function with string 'Welcome to Movie4Us'
    
    SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}              #Utililize 'dictionary' data structure to assign correct suffix to numbers
    def ordinal(tickets_issued):                        #Define function(ordinal) with parameter list 'tickets_issued'
        """Function to assign correct suffix to number"""   #Doc string to describe purpose of function
        if 10 <= tickets_issued % 100 <= 20:            #if statement for numbers between 10 & 20 for any multuple of 100 as these don't follow the normal counting scheme
            suffix = 'th'                               #Assign suffix 'th' to these numbers
        else:                                           #else staement for all other numbers. 
            suffix = SUFFIXES.get(tickets_issued % 10, 'th')    #Utilize dictionary get method to return value 'th' if key 'ticket_issued % 10' isn't satisfied.
        return str(tickets_issued) + suffix             #return statement to execute function. Converts 'tickets_issued' to a string & adds the suffix
    
    
    #Calls print function at each iteration of the while loop. Inserts the following with the use of a Tuple: Calls the ordinal function with current value of 'tickets =_issued' & also variable 'tickets_remaining.
    print("You are the %s user. The number of remaining tickets is now %s" %(ordinal(tickets_issued), tickets_remaining))   
    
print("There are no more ticket")                       #Calls print function when the while loop conditions have been exhausted.