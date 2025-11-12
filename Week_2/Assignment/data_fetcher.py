import requests


def fetch_user_name(user_id):
    response = requests.get(f"https://example.com/api/users/{user_id}")
    return response.json()["name"]
