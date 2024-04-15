#!/usr/bin/python3
"""A POST request with urllib"""
import urllib.request, sys, urllib.parse
data = {'email': sys.argv[2])
data = urllib.parse.urlencode(data)
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(req) as response:
    new_response = response.read()
print(new_response.decode('utf-8'))

