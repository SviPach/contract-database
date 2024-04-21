"""Checks the entered value."""

import datetime


def int_positive_check(x):
    """
    Check if the character(s) is a positive integer.

    Returns:
    - False - the character(s) is not a positive integer.
    - True - the character(s) is a positive integer.
    >>> int_positive_check(2)
    True
    >>> int_positive_check(s)
    False
    """
    try:
        isinstance(int(x), int)
    except ValueError:
        print("!!! Error! Not int.")
        return False

    if int(x) <= 0:
        print("!!! Error! Can't be less or equal 0.")
        return False

    return True


def float_check(x):
    """
    Check if the character(s) is a floating point number.

    Returns:
    - False - the character(s) is not a floating point number.
    - True - in case the character(s) is a floating point number.
    >>> float_check(2.2)
    True
    >>> float_check(11)
    True
    >>> float_check(ten)
    False
    """
    try:
        isinstance(float(x), float)
    except ValueError:
        print("!!! Error! Not float.")
        return False
    return True


def date_check(x):
    """
    Check if the string is a date if format dd-mm-yyyy.

    Returns:
    - False - the string is not a date in format dd-mm-yyyy.
    - True - the string is a date in format dd-mm-yyyy.
    >>> date_check(05-01-2024)
    True
    >>> date_check(2024-01-05)
    False
    >>> date_check(5 January)
    False
    """
    try:
        datetime.datetime.strptime(x, '%d-%m-%Y')
    except ValueError:
        print("!!! Error! Not dd-mm-yyyy.")
        return False
    return True
