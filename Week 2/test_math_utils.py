from math_utils import double


def test_double_positive():
    assert double(5) == 10


def test_double_zero():
    assert double(0) == 0


def test_double_negative():
    assert double(-3) == -6
