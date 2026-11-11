def mean(values: list) -> float:
    """Calculates the mean of given values.
    Args: values: list = A list containing values to be calculated.
    Example: mean of values=[2, 4, 4, 4, 5, 5, 7, 9] equals 5.     
    """
    assert values != [], "There is no value to be calculated."
    total = 0
    for value in values:
        total += value
    mean = total / len(values)
    return mean

def variance(values: list) -> float:
    """Calculates the variance of given values.
    Args: values: list = A list containing values to be calculated.
    Example: variance of values=[2, 4, 4, 4, 5, 5, 7, 9] equals 4.
    """
    assert values != [], "There is no value to be calculated."
    total = 0
    for value in values:
        total += (value - mean(values)) ** 2 
    variance = total / len(values)
    return variance

def std(values: list) -> float:
    """Calculates std of given values.
    Args: values: list = A list containing values to be calculated.
    Example: std of values=[2, 4, 4, 4, 5, 5, 7, 9] equals 2.
    """
    assert values != [], "There is no value to be calculated."
    std = variance(values) ** 0.5
    return std

test = [2, 4, 4, 4, 5, 5, 7, 9]
assert round(mean(test), 2) == 5.00
assert round(variance(test), 2) == 4.00
assert round(std(test), 2) == 2.00