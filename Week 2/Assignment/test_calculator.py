import pytest
from calculator import multiply_positive_numbers


def test_both_positive():
    assert multiply_positive_numbers(2, 3) == 6


def test_negative_input():
    with pytest.raises(ValueError):
        multiply_positive_numbers(-4, 6)


def test_not_a_number_input():
    with pytest.raises(TypeError):
        multiply_positive_numbers("a", 7)
