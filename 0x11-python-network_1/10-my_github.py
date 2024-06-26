#!/usr/bin/python3
"""Basic Authentication"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    req = \
        requests.get('https://api.github.com/user', auth=(username, password))
    if req.status_code == 200:
        user = req.json()
        print(user.get('id'))
    else:
        print('None')
