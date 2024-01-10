#!/usr/bin/python3
"""Module writes a str. to a text file"""


def write_file(filename="", text=""):
    """opens a text file in write mode and UTF-8 format"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
