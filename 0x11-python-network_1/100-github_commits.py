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
    commits = commits.json()
    for m in range(10):
        if commits[m] in commits:
            print("{}: {}".format(commits[m].get('sha'), commits[m].get('commit')['author']['name']))
