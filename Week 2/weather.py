import requests


def get_weather(city):
    response = requests.get(f"https://api.example.com/weather/{city}")
    return response.json()["temperature"]
