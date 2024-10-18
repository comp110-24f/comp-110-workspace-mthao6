__author__ = "730749520"

def find_and_remove_max(vals: list[int]) -> int:
    if not vals: 
        return -1 # If input is empty
    
    max_value = max(vals)

    while max_value in vals: # remove all instances of the largest val
        vals.remove(max_value)

    return max_value