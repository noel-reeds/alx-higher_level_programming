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
    chars = ".?:"
    if  chars[0] in text or chars[1] in text or chars[2] in text:
        print()
