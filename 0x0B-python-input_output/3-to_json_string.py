#!/usr/bin/python3
import json
"""Module converts a Python data structure to JSON format"""


def to_json_string(my_obj):
    """converts an obj. into a json string"""
    json_str = json.dumps(my_obj)
    return json_str
