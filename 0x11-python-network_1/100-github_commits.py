#!/usr/bin/python3
"""Lists commits of a user's repository"""

import sys
import requests
if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    api = f"https://api.github.com/repos/{owner_name}/\
{repository_name}/commits"
    commits = requests.get(api)
    r = commits.json()
    for m in range(10):
        if m < len(r):
            print(f"{r[m].get('sha')}: {r[m].get('commit')['author']['name']}")
