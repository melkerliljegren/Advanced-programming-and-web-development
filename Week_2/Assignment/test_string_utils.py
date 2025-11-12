import pytest
from string_utils import count_vowels


def test_vowel_basic():
    assert count_vowels("banana") == 3


def test_vowel_uppercase():
    assert count_vowels("ApPlE") == 2


def test_vowel_raises_typeerror_on_none_string():
    with pytest.raises(TypeError):
        count_vowels(1234)
