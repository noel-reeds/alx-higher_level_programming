#!/usr/bin/python3
"""Exceptions"""

import urllib.request
import sys
if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            res = response.read()
        print('Index')
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
