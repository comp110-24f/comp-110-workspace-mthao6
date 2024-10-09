

__author__ = "730749520"

"""Creating lists"""

def all(vals: list[int], target: int) -> bool:
    if len(vals) == 0: # If list is empty return False
        return False
    
    for val in vals:
        if val != target:
            return False # Return False if any val doesnt match target
        
    return True # If Loop completes, val matches target and returns True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    
    max_value = input[0]
    # goes through the list to find max val
    for number in input[1:]:
        if number > max_value:
            max_value = number
    return max_value

def is_equal (list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2): # Check if length in both lists are =
        return False
    
    # Compare each elem in both lists at each idx
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True # If all elems match return True

def extend(list1: list[int], list2: list[int]) -> None:
    for element in list2:
        list1.append(element)


    