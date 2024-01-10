#!/usr/bin/python3
"""Module decodes a JSON str. to a Python obj.."""
import json


def from_json_string(my_str):
    """converts a JSON str to a Python obj.."""
    python_obj = json.loads(my_str)
    return python_obj
