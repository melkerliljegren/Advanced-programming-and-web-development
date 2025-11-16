from weather_station import WeatherStation
import os

def test_temperature_index(weather_data):
    station = WeatherStation()
    for temps, factor, expected in weather_data:
        assert round(station.temperature_index(temps, factor), 1) == expected
        
        
def test_process_and_save(tmp_path):
    station = WeatherStation()
    temps = [20, 22, 24]
    factor = 1.1
    station.save_report = lambda index, filename: tmp_path / filename # Mock save
    path = station.process_and_save(temps, factor, "mock_report.txt")
    assert path is None # process_and_save does not return value