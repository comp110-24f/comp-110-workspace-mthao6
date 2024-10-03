

__author__ = "730749520"

def get_coords(xs: str, ys: str) -> None:
    i = 0
    while i < len(xs): # The outer loop for each character in xs
        j=0
        while j < len(ys): # The inner loop for each character in ys
            print(f"({xs[i]},{ys[j]})") # Prints the pair 
            j += 1 # Moves to the next character in ys 
        i += 1 # Moves to the next character in xs
