#!/usr/bin/python3
"""Module appends a str. to a text file"""


def append_write(filename="", text=""):
    """opens a file in append mode and UTF-8 format"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
