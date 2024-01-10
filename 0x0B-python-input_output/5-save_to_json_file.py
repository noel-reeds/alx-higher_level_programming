#!/usr/bin/python3
"""Module dumps a Python obj. to a text file.."""
import json


def save_to_json_file(my_obj, filename):
    """converts a Python obj. to a JSON str and writes it to a text file"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
