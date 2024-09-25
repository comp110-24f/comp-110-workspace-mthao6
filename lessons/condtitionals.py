"""Practing condtionals."""


def less_than_10(num: int) -> bool:
    """Tell us if num < 10."""
    if num < 10:  # check if this is true
        print("Small number!")
    else:
        print("Big number!")
    print("This is the end of the function!")


def wake_up(alarm: bool) -> str:
    """Return a message if alarm is going off."""
    if alarm is True:
        return "Wake Up!!"
    else:
        return "Go back to bed its not worth."


print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is first character of word."""
    if word[0] == letter:
        return "match"
    else:
        return "no match"


check_first_letter(word="happy", letter="h")
