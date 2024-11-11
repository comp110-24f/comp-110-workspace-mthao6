
__author__ = "730749520"

"""File to define Bear class."""

class Bear:
    def __init__(self) -> None:
        """Intializing attributes"""
        self.age: int = 0
        self.hunger_score: int = 0
    
    def one_day(self) -> None:
        """Hunger increases as hunger_score decreases"""
        self.age += 1
        self.hunger_score -=1 
        
    def eat(self, num_fish: int) -> None:
        """Increases hunger_score by # of fish eaten"""
        self.hunger_score += num_fish