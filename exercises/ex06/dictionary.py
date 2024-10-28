"""Writting dictionary funcs"""

__author__ = "730749520"

def invert(input_dict: dict[str,str]) -> dict[str, str]:
    inverted_dict = {}
    for key, value in  input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate key found when inverting!")
        inverted_dict[value] = key

    return inverted_dict 

def favorite_color(favorites: dict[str, str]) -> str: # Dict to store color counts
    color_count = {}
    for color in favorites.values():
        if color in color_count: # Count each color occurence
            color_count[color] += 1
        else: 
            color_count[color] = 1
    max_count = 0 
    favorite_color = "" # Int with an empty str

    for color in favorites.values():
        if color_count[color] > max_count:
            max_count = color_count[color]
            favorite_color = color
        elif color_count[color] == max_count and favorite_color == "": # If tie, select first color that appeared
            favorite_color = color 

    return favorite_color 

def count(values: list[str]) -> dict[str, int]:
    result = {} # Int an empty dict to store the counts 

    for item in values: # Loop thru each item in input list
        if item in result: 
            result[item] += 1
        else: 
            result[item] = 1

    return result # Return results of dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorize words into dic based on starting letters"""
    result = {}

    for word in words: 
        first_letter = word[0]. lower() # Convert first letter to lowercase
         
        if first_letter not in result: 
            result[first_letter] = [] # Create a new list for this letter

            result[first_letter].append(word) # Append word to the corresponding list
    return result 

def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
        if day not in attendance: # Checks if day exists in the dic
            attendance[day] = []

        attendance[day].append(student) # Adds the student to the attendance list for the day