from weather import get_weather


def generate_report(city):
    temp = get_weather(city)
    return f"The temperature in {city} is {temp}°C."
