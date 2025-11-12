from greeting import generate_greeting


def test_generate_greeting(monkeypatch):
    called = {"count": 0}

    def mock_fetch_user_name(user_id):
        called["count"] += 1
        return "Melker"

    monkeypatch.setattr("greeting.fetch_user_name", mock_fetch_user_name)

    result = generate_greeting(5)

    assert result == "Hello, Melker!"
    assert called["count"] == 1


def test_generate_greeting_handles_connection_error(monkeypatch):
    def mock_fetch_user_name(user_id):
        raise ConnectionError("Error fetching user.")

    monkeypatch.setattr("greeting.fetch_user_name", mock_fetch_user_name)

    result = generate_greeting(5)
    assert result == "Error fetching user."
