from data_fetcher import fetch_user_name


def generate_greeting(user_id):
    try:
        name = fetch_user_name(user_id)
    except ConnectionError:
        return "Error fetching user."
    return f"Hello, {name}!"
