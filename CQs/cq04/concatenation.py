

__author__ = "730749520"

def concat(str1:str, str2:str) -> str:
    return str1+str2 # Concatenates two strings and returns the results
    

# Global variables
word1:str = "happy"
word2:str = "tuesday"


if __name__ == "__main__": # Will call the function if this is run directly
    print(concat(word1,word2)) # Results = "happytuesday"
