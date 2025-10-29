from weather_report import generate_report


def test_generate_report(monkeypatch):
    def mock_get_weather(city):
        return 22

    # Replace the real function with the mock
    monkeypatch.setattr("weather_report.get_weather", mock_get_weather)

    result = generate_report("Gothenburg")
    assert result == "The temperature in Gothenburg is 22°C."
