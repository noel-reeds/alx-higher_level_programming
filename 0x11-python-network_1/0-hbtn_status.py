#!/usr/bin/python3
import urllib.request
req_object = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req_object) as req:
    page = req.read()
print('Body response:\n\t- type: {}\n\t- content: {}\n\t- \
utf8 content: {}'.format(type(page), page, page.decode('utf-8')))
