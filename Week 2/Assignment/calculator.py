def multiply_positive_numbers(a, b):
    if a < 0 or b < 0:
        raise ValueError("Numbers must be positive")
    elif not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("One argument is not a number")
    return a * b
