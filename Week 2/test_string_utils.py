from string_utils import count_vowels


def test_vowel_basic():
    assert count_vowels("hello") == 2


def test_vowel_uppercase():
    assert count_vowels("APE") == 2


def test_vowel_none():
    assert count_vowels("rhytm") == 0
