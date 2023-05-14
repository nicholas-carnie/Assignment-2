

# Code to measure speed and distance travelled by a ball
# enter validation function
def get_input(prompt):
    # Using while loop that runs  until a valid integer is given
    while True:
        try:
            value = int(input(prompt))
            # Checking if the input is less than zero
            if value < 0:
                raise ValueError
            # Return the valid input
            return value
        except ValueError:
            print("\nInvalid input. Please enter a non-negative integer.\n")


try:
    # Ask the value of the speed and minutes from the user 
    speed = get_input("What is the speed of the ball (in metres per minute)?\n")
    minutes = get_input("How many minutes has it travelled?\n")
    
    # Printing the table header
    print("--------------------------------------")
    print("Hour"+"\t"*2+"Distance Travelled")
    print("--------------------------------------\n")

    # Initializing the hour and distance variables
    hour = 1
    distance = speed

    #  Use while loop for each minute and print the hour and distance travelled
    while hour <= minutes:
        print(hour,"\t"*2,distance)
        hour += 1
        distance += speed

# Catch the KeyboardInterrupt exception, which is raised when the user
# presses Ctrl+C to terminate the program
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
