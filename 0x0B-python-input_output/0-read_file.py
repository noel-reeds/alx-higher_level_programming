#!/usr/bin/python3
"""Module reads a text file in UTF-8 and prints it to stdout."""


def read_file(filename=""):
    """opens file in read mode and in UTF-8"""
    with open("filename", "r", encoding="utf-8") as myFile:
        print(myFile.read())
