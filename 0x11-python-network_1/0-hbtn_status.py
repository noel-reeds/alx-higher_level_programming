#!/usr/bin/python3
import urllib
req_object = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req_object) as req_page:
    fetched_page = req_page.read()
