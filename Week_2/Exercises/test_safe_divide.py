import pytest
from Week_2.Exercises.safe_divide import safe_divide


def test_divide_normal():
    assert safe_divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ValueError):
        safe_divide(5, 0)
