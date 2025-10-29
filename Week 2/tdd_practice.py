def add_positive_numbers(a, b):
    if a < 0 or b < 0:
        raise ValueError("Numbers must be positive")
    return a + b
