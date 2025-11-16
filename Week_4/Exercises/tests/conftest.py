import pytest

@pytest.fixture
def weather_data():
    return [
        ([20, 22, 24], 1.1, 27,6),
        ([15, 15, 15], 1.2, 23)
    ]