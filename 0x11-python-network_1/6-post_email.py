#!/usr/bin/python3
"""Okay..a POST request"""

import sys
import requests
if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=payload)
    print(req)
