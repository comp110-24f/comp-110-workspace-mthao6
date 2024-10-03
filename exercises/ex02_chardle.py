"""EX02 Charrdle- Worlde Intro"""

__author__ = "730749520"

import sys # Imports sys to use the sys.exit()

def input_word() -> str:
    word = input("Enter a 5-character word: ") # Prompts user for an input
    if len(word) != 5: # Input needs to be exactly 5 characters
        print("Error: Word must contain 5 characters.") # Will print if not 5 characters
        sys.exit() # Will exit if not 5 characters
    return word

def input_letter() -> str: 
    letter = input("Enter a single character: ")
    if len(letter) != 1: # Checks if input is one character
        print("Error: Character must be a single character.") # Will print if not one character
        sys.exit()
    return letter # Returns the valid letter

def contains_char(word: str, letter: str) -> None:
    print(f"Searching for {letter} in {word}")
    count = 0
    for index in range(len(word)): # Will loop through each character in the word
        if word[index] == letter:
            print(f"{letter} found at index {index}")
            count += 1 # Counts the amount of matches
    if count == 0: # Checks for no match
        print(f"No instances of {letter} found in {word}")
    elif count == 1: # Checks for 1 match
        print(f"1 instance of {letter} found in {word}")
    else: # For if there is more than 1 match 
        print(f"{count} instances of {letter} found in {word}") # Prints if more than 1 match

def main() -> None:
    """Coordinates the charlde game"""
    word_result = input_word()
    letter_result = input_letter()
    contains_char(word_result, letter_result)

if __name__ == "__main__":
    main() # Calls the main function the start the program
