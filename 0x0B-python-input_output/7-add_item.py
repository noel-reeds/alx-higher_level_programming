#!/usr/bin/python3
"""script, adds args to a Python list, saves them in a file"""

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """Adds args to a Python object(list)"""
    try:
        python_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        python_list = []
    python_obj = sys.argv[1:]
    new = python_list + python_obj
    save_to_json_file(new, "add_item.json")
