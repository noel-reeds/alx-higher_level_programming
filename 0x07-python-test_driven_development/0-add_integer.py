#!/usr/bin/python3
"""Module adds two integers.."""


def add_integer(a, b=98):
    """adds two integers and return sum.."""
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        return int(a + b)
