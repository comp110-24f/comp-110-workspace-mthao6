
__author__ = "730749520"

"""File to define Fish class."""

class Fish:
    def __init__(self) -> None:
        """Int a fish with age 0"""
        self.age: int = 0
       

    def one_day(self) -> None:
        """Increasing age by 1 each day"""
        self.age += 1