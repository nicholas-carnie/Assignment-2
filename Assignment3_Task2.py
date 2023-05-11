#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:43:30 2023

@author: carnie
"""

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import time

UserDatabase = {}

def MainMenu():
    checkInput = None
    print("\n" + "===" * 20)
    print("\n**Welcome to Champions Soccer Club**")
    print("Please choose an option from the followings")
    print("1) Add player name and score\n2) Display all the player information and scores\n3) Quit\n")
    print("===" * 20)
    UserChoice = input("Enter you choice \t:")
    try:
        checkInput = int(UserChoice)
        if(checkInput > 3 or checkInput <= 0):
            print("Invalid input.\nProvided Options are 1,2 and 3.\nTry Again.")
            MainMenu()
    except ValueError:
        print("Invalid input.\nEnter a valid Input.")
        MainMenu()

    match checkInput:
        case 1:
            AddPlayerDetails()
        case 2:
            ViewUserDetails()
        case 3:
            print("**GoodBye.. See you again!*")
            exit()
        

def AddPlayerDetails():
    Name = input("\nEnter the player name \t:")
    Score = input("Enter the score \t:")
    try:
        checkScore = int(Score)
        if(checkScore > 100 or checkScore < 0):
            print("\n**Incorrect score** The scores should be from 0-100.\nPlease try again!")
            MainMenu()
    except ValueError:
        print("Invalid Entry.\nTry Again")
        MainMenu()

    UserDatabase[Name] = Score
    UserSelection()


def UserSelection():
    userInput = str(input("Do you want to add another player? Enter Y for Yes, N for  No\t:  "))
    if(userInput.upper() == "Y"):
        AddPlayerDetails()
    elif(userInput.upper() == "N"):
        MainMenu()
    elif(userInput.upper() != "Y" or userInput.upper() != "N"):
        print("Invalid selection.\nTry Agian")
        UserSelection()


def ViewUserDetails():
    print("\nPlayer & Score Details")
    print("\n" + '-' * 30 + "\n")
    print("Player" + "\t"*2 + "Score")
    for item in UserDatabase:
        print(item  + "\t"*2 + UserDatabase[item])
    time.sleep(2.0)    #This gives the user a bit of time to view records displayed.
    MainMenu()


# Calling the Entry point of the applicatiion.
MainMenu()
