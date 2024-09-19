def divide(a, b):
    assert b != 0, "b should not be zero"
    return a / b


result = divide(10, 0)  # This will raise an AssertionError
