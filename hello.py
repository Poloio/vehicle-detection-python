import random
import collections

def square(number):
    """Calculates the square of a number

    Args:
        number (int): the numebr to calculate its square exponent.

    Returns:
        int: the square compponent of the number.
    """
    return number**2

def maximum(value1, value2, value3):
    """Calculate maximum value between three numbers

    Args:
        value1 (int): First value
        value2 (int): Second value
        value3 (int): Third value
    """
    max_value = max(value1, value2, value3)
    return(max_value)

def roll_calculator():
    """Roll 6-face die 6.000.000 times and return all faces occurrences in a list. 

    Returns:
        list: Each one of the faces (1-6) occurrence list.
    """
    occurrences = [0,0,0,0,0,0]
    for roll in range(6_000_000):
        face = random.randrange(1,7)
        occurrences[face-1] += 1
    return occurrences
    
print (roll_calculator())