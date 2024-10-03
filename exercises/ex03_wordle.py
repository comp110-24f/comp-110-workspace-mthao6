

__author__ = "730749520"

def main(secret: str) -> None:
    """The entry point of the program and the main loop"""
    turns = 0 # Number of turns taken by player
    max_turns = 6 # Max turns is 6
    won = False # Indictes the player has not won yet

    while turns < max_turns and not won: # Loops until player wins or max turn is reached
        turns += 1 # Makes the turn amount increase by 1 each time it loops
        print(f"=== Turn {turns}/{max_turns} ===") # displays the amount of turns they have out of 6

        guess = input_guess(len(secret))

        print(emojified(guess, secret))# Will display the results with emojis

        if guess == secret: # Checks to see if the guess is correct 
            won = True
            print(f"You won in {turns}/{max_turns} turns!")
    if not won: 
        print(f"X/{max_turns} - Sorry, try again tomorrow!") # Will print if the player didnt win after 6 tries

def input_guess(secret_word_len: int) -> str: 
    guess = "" # Initialize an empty guess to start loop
    while len(guess) != secret_word_len: # Continue asking for input until user has given the correct length
        guess = input(f"Enter a {secret_word_len} character word: ") # Ask for an input of a word of the required length
        if len(guess) != secret_word_len: # If length is incorrect print and ask again
            print(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess # Once it is the correct length return wanted guess


 
def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if single character (char_guess) is found in the secret_word"""
    assert len(char_guess) == 1 # Ensures that char_guess is one character
    i=0
    while i < len(secret_word): # Loop thru each character in secret_word
        if secret_word[i] == char_guess: # Checks if current char is a match 
            return True # If a match returns True
        i += 1 # Move to the next character in the index
    return False 

def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C" # Letter is not included in secret
    GREEN_BOX: str = "\U0001F7E9" # Indicates correct letter
    YELLOW_BOX: str = "\U0001F7E8" # Indicates a correct letter in the wrong position

    result = ""
    i=0
    while i < len(guess):
        if guess[i] == secret[i]: # Checks if character is correct and in correct position
            result += GREEN_BOX

        elif contains_char(secret, guess[i]): # Checks if character is correct but in the wrong position
            result += YELLOW_BOX

        else: 
            result += WHITE_BOX # Appends white box for letter not in secret
        i += 1 # Move to the next char
    return result

if __name__ == "__main__":
    main(secret="codes") # Calls the main function the start the program
        

