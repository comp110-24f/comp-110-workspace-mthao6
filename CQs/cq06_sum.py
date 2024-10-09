__author__ = "730749520"


"""Summing the elements of a list using different loops""" 

def w_sum(vals: list [float]) -> float:
    total = 0.0
    i = 0
    while i < len(vals): # Loops until indx reach ends of list
        total += vals[i] # Add current element to the total
        i += 1 # Will move to next element
    return total

def f_sum(vals: list [float]) -> float: 
    total = 0.0
    for val in vals: # Loop directly over each val in list
        total += val
    return total

def f_range_sum(vals: list [float]) -> float:
    total = 0.0
    for i in range(len(vals)): #Loop through the indices
        total += vals[i] # Acess the element at each index
    return total


