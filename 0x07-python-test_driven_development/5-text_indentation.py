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

    if '.' not in text and '?' not in text and ':' not in text:  # check..
        print(text)
    iter_index = 0
    max_index = len(text) - 1
    for index, value in enumerate(text):
        if value in chars:
            print(text[iter_index:index + 1])
            print()
            iter_index = index + 2
            if iter_index < max_index and text[max_index] not in chars:
                print(text[iter_index:max_index+1])
