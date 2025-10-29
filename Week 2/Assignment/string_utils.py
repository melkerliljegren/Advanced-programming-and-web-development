def count_vowels(text):
    vowels = "aeiou"
    count = 0

    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    for char in text.lower():
        if char in vowels:
            count += 1
    return count
