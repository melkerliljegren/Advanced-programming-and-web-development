def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide be zero")
    return a / b
