import time                                         #Imports time module

UserDatabase = {}                                   #Creates dictionary for storing players name & score

def MainMenu():
    """Function which gives main menu"""            #Doc string which describes purpose of function
    checkInput = None                               #Resets selection each time function is called
    print("\n" + "===" * 20)
    print("\n**Welcome to Champions Soccer Club**")
    print("Please choose an option from the followings")
    print("1) Add player name and score\n2) Display all the player information and scores\n3) Quit\n")
    print("===" * 20)
    UserChoice = input("Enter you choice \t:")      #User enters either 1, 2 or 3 
    try:                                            #Try/except statement to reduce program crash in case of incorrect selection
        checkInput = int(UserChoice)
        if(checkInput > 3 or checkInput <= 0):      #Checks if user selection is outside range. Returns to start of function.
            print("Invalid input.\nProvided Options are 1,2 and 3.\nTry Again.")
            MainMenu()
    except ValueError:
        print("Invalid input.\nEnter a valid Input.")
        MainMenu()

    match checkInput:                               #Match/case statement to control flow of program
        case 1:
            AddPlayerDetails()
        case 2:
            ViewUserDetails()
        case 3:                                     #Exit selection to end program
            print("**GoodBye.. See you again!*")
            exit()
        

def AddPlayerDetails():
    """Function to add players name & score (Case #1)"""        #Doc string which describes purpose of function
    Name = input("\nEnter the player name \t:")
    Score = input("Enter the score \t:")
    try:                                                        #Try/except statement to reduce program crash in case of incorrect selection
        checkScore = int(Score)
        if(checkScore > 100 or checkScore < 0):
            print("\n**Incorrect score** The scores should be from 0-100.\nPlease try again!")
            MainMenu()
    except ValueError:
        print("Invalid Entry.\nTry Again")
        MainMenu()

    UserDatabase[Name] = Score                                  #Assigns Name & Score as key value pairs to dictionary
    UserSelection()                                             #Calls UserSelection function after AddPlayerDetails function ends


def UserSelection():
    """Function which directs user to either MainMenu or AddPlayerDetails functions"""      #Doc string which describes purpose of function
    userInput = str(input("Do you want to add another player? Enter Y for Yes, N for  No\t:  "))
    if(userInput.upper() == "Y"):                               #Checks user input. Converts to upper case
        AddPlayerDetails()                                      #Function called for 'Y' selection
    elif(userInput.upper() == "N"):                             #Checks user input. Converts to upper case
        MainMenu()                                              #Function called for 'N' selection
    elif(userInput.upper() != "Y" or userInput.upper() != "N"):     #Condition for incorrect user input
        print("Invalid selection.\nTry Agian")
        UserSelection()                                         #Function called for incorrect selection
                           
            
def ViewUserDetails():
    """Function to view all entries for Userselection function (Case #2)"""                 #Doc string which describes purpose of function
    print("\nPlayer & Score Details")
    print("\n" + '-' * 30 + "\n")
    print("Player" + "\t"*2 + "Score")
    for item in UserDatabase:                                   #for loop to display all values for UserDatabase
        print(item  + "\t"*2 + UserDatabase[item])
    time.sleep(2.0)                                             #This gives the user a bit of time to view records displayed.
    MainMenu()                                                  #Calls MainMenu function after ViewUserDetails function ends


                                   
MainMenu()                                                      # Calling the Entry point of the applicatiion.
