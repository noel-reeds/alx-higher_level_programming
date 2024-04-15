#!/usr/bin/python3
"""Finds the peak in a list of integers"""


def find_peak(list_of_integers):
    """Returns peak value"""
    if list_of_integers:
        peak = list_of_integers[0]
        for m in range(len(list_of_integers)):
            if list_of_integers[m] > peak or \
                    list_of_integers[m-1] < list_of_integers[m]:
                peak = list_of_integers[m]
        return peak
    return None
