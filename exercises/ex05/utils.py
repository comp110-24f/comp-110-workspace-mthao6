__author__ = "730749520"

def only_evens(vals: list[int]) -> list[int]:
    result = [] # Create new list to store even numbs
    for i in range(len(vals)): # Go through input list
        if vals[i] % 2 == 0: # Checks if current elem is even
            result.append(vals[i]) # Append even elem to result list
    return result

def sub(vals: list[int], start: int, end: int) -> list[int]:
    """Generates a subset of input list between start and end"""
    if len(vals) == 0 or start >= len(vals) or end <= 0:
        return []
    
    if start < 0:
        start = 0
    if end > len(vals):
        end = len(vals)

    result = []
    for i in range(start, end):
        result.append(vals[i])

    return result

def add_at_index(vals:list[int], element: int, index: int) -> None:
    """Insert an elem at given index in listm mutates the list in replace"""
    if index < 0 or index > len(vals): # Checks if indx is out of bounds
      raise IndexError("Index is out of bounds for the input list") # Raise an indexerror with a message

    vals.append(0) # Extends the list by 1 

    for i in range(len(vals) - 1, index, -1): # Shifts elem to right to make space for new elem
        vals[i] = vals[i-1]

    vals[index] = element # Places new elem at the correct position