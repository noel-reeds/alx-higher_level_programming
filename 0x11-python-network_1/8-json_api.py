#!/usr/bin/python3
"""yet another POST request"""

import sys
import requests
if __name__ == "__main__":
    if len(sys.argv) < 2:
        payload = {'q': ""}
        print('No result')
    else:
        payload = {'q': sys.argv[1]}
        req = requests.post('http://0.0.0.0:5000/search_user', payload)
        if req.headers['Content-Type'] == 'application/json':
            if req.text:
                req_dict = eval(req.text)
                print('[{}] {}'.format(req_dict['id'], req_dict['name']))
            else:
                print('No result')
        else:
            print('Not a valid JSON')
