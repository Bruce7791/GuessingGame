# A program that gives the user a chance to guess a number between 1 and 100
# And also can watch the computer do it with a random number generator. 

import random

while True:

    print("Welcome to Bruce's Number Guessing Game")
    print()
    print("Try to guess a number between 1 and 100 or watch the computer do it instead")
    print()
    print("1. You guess the number")
    print("2. The computer guesses the number")

    print()

    # Take input from the user 
    choice = input("Enter choice(1/2): ",)
    print()

    if choice == '1':
        print("Try to guess a number between 1 and 100 in as a few trys as possible.")
        print()
        # Get a random number between 1 and 100.

        hiddenNumber = random.randint(1, 100)

        # Create a user guess and give is a value that can't be correct.

        userGuess = 0
        guesses = 0
        # Repeat until the guess is correct.

        while not userGuess == hiddenNumber:
            # Get the user's input as an integer.
            userGuess = int(input("Guess the number: " ))
            # Check if the guess is too high.
            if userGuess > hiddenNumber:
                print("Too high")
            # Check if the guess is too low.
            elif userGuess < hiddenNumber:
                print("Too low")
            # If the guess is right. 
            else:
                print("That's right!")
            guesses+=1
        print("You took {} guesses!".format(guesses))
        print()
        

    elif choice == '2':
        print("Watch the computer try to guess a random number between 1 and 100 with a random number generator.")
        print()
        # Get a random number between 1 and 100.

        hiddenNumber = random.randint(1, 100)

        # Create a user guess and give is a value that can't be correct.

        userGuess = 0
        guesses = 0
        # Repeat until the guess is correct.

        while not userGuess == hiddenNumber:
            # Get the user's input as an integer.
            userGuess = random.randint(1, 100)
            # Check if the guess is too high.
            if userGuess > hiddenNumber:
                print("Too high")
            # Check if the guess is too low.
            elif userGuess < hiddenNumber:
                print("Too low")
            # If the guess is right. 
            else:
                print()
                print("That's right!")
                print()
                print("The hidden number was: ", hiddenNumber)
            guesses+=1
        print("The computer took {} guesses to find it!".format(guesses))
        print()
        
       
           
       
        
            
        
            
        
        

            
        
        
            
        
        
            
        
            
            
    
    
        
    
    
        
    
        
        
            
                
            
            
                
            
                
                
            


    
    