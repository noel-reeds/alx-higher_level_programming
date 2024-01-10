#!/usr/bin/python3
"""converts a JSON file into an obj.."""
import json


def load_from_json_file(filename):
    """converts a 'JSON text file' to a Python object.."""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        python_obj = json.load(myFile)
        return python_obj
