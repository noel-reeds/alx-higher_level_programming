#!/usr/bin/python3
"""script, adds args to a Python list, saves them in a file"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import json
import sys


if __name__ == "__main__":
    """Adds args to a Python object(list)"""
    python_obj = sys.argv[1:]
    save_to_json_file(python_obj, "add_item.json")
