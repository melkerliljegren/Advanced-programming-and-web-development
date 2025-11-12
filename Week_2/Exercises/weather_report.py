from Week_2.Exercises.weather import get_weather


def generate_report(city):
    try:
        temp = get_weather(city)
        return f"The temperature in {city} is {temp}°C."
    except ConnectionError:
        return "Error fetching weather data."
