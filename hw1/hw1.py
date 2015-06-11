# Python HW 1
# Tim Whitfield

name = input("Hi, what is your name?\n")
print("Hello, " + name + "! Let's play a game!")
playagain = True

# Main loop executes once for each game
while (playagain):
    print("Think of a random number from 1 to 100, and I'll try to guess it!")
    lowest = 1
    highest = 100
    guessed = False
    tries = 0
    # Loop for CPU guesses
    while (not guessed):
        tries = tries + 1
        if (highest == 100 and lowest == 99):
            guess = 100
        else:
            guess = (highest + lowest)//2
        answer = input("Is it " + str(guess) + "? (yes/no) ")
        if (answer == "no"):
            answer = input("Is the number larger than " + str(guess) + "? ")
            # Adjust lowest/highest values accordingly 
            if (answer == "yes"):
                lowest = guess
            elif (answer == "no"):
                highest = guess
        # Exit loop when guessed
        elif (answer == "yes"):
            guessed = True
    print("Hooray! I got it in " + str(tries) + " tries!")
    answer = input("Do you want to play again? ")
    # Exit main loop if player wants to quit
    if (answer == "no"):
        print("Bye-bye!")
        playagain = False
        
        
    
