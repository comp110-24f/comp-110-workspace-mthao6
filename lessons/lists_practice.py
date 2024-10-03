"""Practicing lists"""

my_numbers: list[float] = [] # Literal
my_numbers: list[float] = list() # Constructor 

# Adding an item to a list
my_numbers.append(1.5)



# Creating an already populated list
game_points: list[int] = [102, 86, 94]

#Indexing 
game_points[0]
print(game_points[2]) # Will print 94 bc it is index 2

#Modifying elements replacing 86 with 72
game_points[1] = 72
print(game_points)

#Getting the length 
print(len(game_points))

#Remove item from list

game_points.pop(1)
print(game_points)

def display(number: str) -> None:
    
display: list[int] = []