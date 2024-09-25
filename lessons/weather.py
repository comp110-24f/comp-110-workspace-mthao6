def get_weather_report() -> str:
    """Determine what to do depending on the weather"""
    weather: str = input("What is the weather?")
    if weather == "cold" or weather == "rainy":
        print("Bring a jacket")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather")
    return weather
