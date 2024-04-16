#!/usr/bin/python3
"""Error codes"""

import sys
import requests
if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
    except HTTPError as err:
        if req.status_code >= 400:
            print('Error code: {}'.format(req.status_code))
