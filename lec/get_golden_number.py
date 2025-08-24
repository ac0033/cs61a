def improve(update, close, guess):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def get_golden_number(guess=1.0):
    """Return the golden number, which is the limit of the ratio of successive Fibonacci numbers.

    >>> approx_eq(get_golden_number(), 1.618033988749895)
    True
    """
    return improve(golden_update, square_close_to_successor, guess)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(get_golden_number())
    # 1.618033988749895
    # The golden number is the limit of the ratio of successive Fibonacci numbers.
    # It is also known as the golden ratio or phi (φ).