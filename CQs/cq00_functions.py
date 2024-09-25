__author__ = "730749520"


def mimic(message: str) -> str:
    """Return message"""
    return "" + message + ""


def main() -> None:
    """Print mimic"""
    print(mimic(message=input("What is your message")))


if __name__ == "__main__":
    main()
