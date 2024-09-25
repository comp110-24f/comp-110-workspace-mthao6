"""Creating a tea party!"""

__author__ = "730749520"


def main_planner(guests: int) -> None:
    """Calls the functions together and creates outputs"""
    tea_bag_count = tea_bags(people=guests)
    treat_count = treats(people=guests)
    total_cost = cost(tea_count=tea_bag_count, treat_count=treat_count)
    # I have to call the functions for the results
    print("A Cozy Tea Party for " + str(guests) + " People!\n")
    print("Tea bags: " + str(tea_bag_count))
    print("Treats: " + str(treat_count))
    print("Cost: $" + f"{total_cost:.2f}")
    # This rounds the decimal to 2 decimal places.


def tea_bags(people: int) -> int:
    """The amount of teabags needed for people"""
    return people * 2


def treats(people: int) -> int:
    """The amount of treats needed for people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of the teabags and treats"""
    return float(tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
