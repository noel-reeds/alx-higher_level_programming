#!/usr/bin/python3
"""A POST request with requests.."""

import requests
import sys
if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    header = req.headers.get('X-Request-Id')
    print(header)
