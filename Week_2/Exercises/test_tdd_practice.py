import pytest
from tdd_practice import add_positive_numbers


def test_add_both_positive():
    assert add_positive_numbers(2, 5) == 7


def test_negative_input():
    with pytest.raises(ValueError):
        add_positive_numbers(-1, 5)
