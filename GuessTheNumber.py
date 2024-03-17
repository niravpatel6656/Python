import random

# ASCII art logo
logo = '''
  ____                       _   _          
 / ___|_   _  ___  ___ ___  | |_| |__   ___ 
| |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \
| |_| | |_| |  __/\__ \__ \ | |_| | | |  __/
 \____|\__,_|\___||___/___/  \__|_| |_|\___|
| \ | |_   _ _ __ ___ | |__   ___ _ __      
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__|     
| |\  | |_| | | | | | | |_) |  __/ |        
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|        
'''
print(logo)

def game(guess):
    # Generate a random number multiplied by 5 between 1 and 20
    random_number = random.randrange(1, 20) * 5
    print(random_number)  # For testing purposes
    
    # Flag to track if the user has won
    won = False
    
    # Loop until the user runs out of guesses or correctly guesses the number
    while guess > 0 and not won:
        # Ask the user to guess the number
        guessed_number = int(input("\nGuess the Number: "))
        
        # Check if the guessed number is higher than the random number
        if guessed_number > random_number:
            print(f"It's too high\n\nRemaining Guesses: {guess - 1}")
        # Check if the guessed number is lower than the random number
        elif guessed_number < random_number:
            print(f"It's too low\n\nRemaining Guesses: {guess - 1}")
        # Check if the guessed number is equal to the random number
        elif guessed_number == random_number:
            print("You won!")
            won = True  # Set the flag to True since the user has won
        
        # Decrement the remaining guess count
        guess -= 1
    
    # If the user runs out of guesses without correctly guessing the number
    if guess == 0 and not won:
        print("\nSorry, you lose. Better luck next time")

def the_game():
    # Ask the user to choose the game difficulty level
    game_choice = input("\nChoose your level 'Hard' or 'Easy': ").lower()

    # Start the game based on the user's choice
    if game_choice == "hard":
        game(5)  # Set 5 guesses for hard level
    elif game_choice == "easy":
        game(10)  # Set 10 guesses for easy level
    else:
        print("Please enter a valid choice")
    
    # Ask if the user wants to play again game
    play_again = input("\nDo you want to play again? Yes or No: ").lower()
    if play_again == "yes":
        the_game()
    else:
        print("Goodbye")

# Start the game
game_start = input("Do you want to play the game? Yes or No: ").lower()
if game_start == "yes":
    the_game()
else:
    print("Goodbye")
