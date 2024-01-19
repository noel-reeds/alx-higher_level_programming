#!/usr/bin/python3
"""
Module prints new lines after chars..
"""


def text_indentation(text):
    """
    Function prints 2 new lines after chars ., ? and :

    Args:
        text(str):

    Returns:

    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    chars = '.?:'

    iter_index = 0
    for index, value in enumerate(text):
        for char in chars:
            if value == char:
                print(text[iter_index:index + 1])
                print()
                iter_index = index + 2
