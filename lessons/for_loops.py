"""For loops + syntax practicing"""

pets: list[str] = ["Louie", "Bo", "Bear"]
# tell each pet they are good boy
for animal in pets:
    print(f"Good boy, {animal}!")

"""Print out index and name"""
names: list[str] = ["Alyssa", "Joe", "Momma"]
for idx in range(0,len(names)):
    print(str(idx) + ": " + names[idx])