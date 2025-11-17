import pytest

@pytest.fixture
def sample_numbers():
    return {
        "a": 5,
        "b": 2,
        "multiplier": 3,
        "expected": 21
    }