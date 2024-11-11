
__author__ = "730749520"

"""File to define River class."""


from exercises.ex07.bear import Bear
from exercises.ex07.fish import Fish

class River:
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears:int) -> None:
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = [Fish() for _ in range(num_fish)]
        self.bears: list[Bear] = [Bear() for _ in range(num_bears)]
        # populate the river with fish and bears

    def view_river(self) -> None:
        """Prints current state of the river, including the day and pop of fish"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
      
            
    def one_river_day(self) -> None:
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()

        self.bears_eating() # Simulates bears eating
        self.check_ages() # Removes old fish and bear
        self.check_hunger() # Removes hungry bears from river
        self.repopulate_fish()
        self.repopulate_bears()
        
    
    def one_river_week(self) -> None:
        """Simulate a single day in the river"""
        for _ in range(7):
            self.one_river_day()
            
    def check_ages(self) -> None:
        """Removes fish older than 3 days and bears older than 5 days."""
        self.fish = [fish for fish in self.fish if fish.age <=3]
        self.bears = [bear for bear in self.bears if bear.age <=5]
        
    def remove_fish(self, amount: int) -> None:
        """Remove any fish older than 3 days and bear older than 5 days"""
        self.fish = self.fish [amount:] if amount <= len(self.fish) else []
      
    
    def bears_eating(self) -> None:
        """Each bear eats 3 fish if there is at least 5 in river"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3) # Remove 3 fish from river
                bear.eat(3) # Increase bears hunger score by 3

    def check_hunger(self) -> None:
        """Removes bears w hunger score < 0 from river"""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
      
    
    def repopulate_bears(self) -> None:
        """For each pair of bears, add 1 new bear to pop."""
        num_new_bears = len(self.bears) // 2
        self.bears.extend(Bear() for _ in range(num_new_bears))

    def repopulate_fish(self) -> None:
        """For each pair of fish, add 4 new fish to the pop."""
        num_new_fish = (len(self.fish) // 2) * 4
        self.fish.extend(Fish() for _ in range(num_new_fish))
        