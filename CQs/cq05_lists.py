__author__ = "730749520"

"""Mutating functions."""

def manual_append(vals: list[int], value: int) -> None:
    idx: int = len(vals) # Uses lists length to find next index where new val will be added
    vals.append(value) # Extends the list by adding a new value at the next indx

def double(vals:list[int]) -> None:
    idx: int= 0 # Intialize the idx variable to zero
    while idx < len(vals): # Will loop through list as long as idx is less than length of list
        vals[idx] = vals[idx] *2 # Multiply the current element by 2 and update it in the list
        idx +=1 # Index moves to the next element in list

#Global variable list_1
list_1: list[int] = [1,2,3]

list_2: list[int] = list_1 # list_2 references list_1

double(list_2) # Calls the double func w list_2

print("list_1:", list_2)
print("list_2:",list_1)

