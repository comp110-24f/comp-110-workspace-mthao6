__author__ = "730749520"


def guess_a_number() -> None:
    secret=7
    user_input = int(input("Guess a number:"))
    print(f"Your guess was {user_input}.")
    if user_input == secret: 
        print("You got it!!")
    elif user_input < secret: 
        print(f"Your guess was too low! The secret number is {secret}.")
    else: #user_input > secret:
        print(f"Your guess was too high! The secret number is {secret}.")

if __name__== "__main__":
    guess_a_number()
