#!/usr/bin/python3
"""Script adds args to a Python list, saves them in a file"""

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        # checks for a list in the json file
        current = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # if try clause is False, initialize an empty list..
        current = []
    args = sys.argv[1:]
    new = current + args
    save_to_json_file(new, "add_item.json")
