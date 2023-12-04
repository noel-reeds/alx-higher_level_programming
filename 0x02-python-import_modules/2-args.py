#!/usr/bin/python3
import sys
res = len(sys.argv)
if res == 1:
    print('0 arguments.')
elif res == 2:
    print('1 argument')
    print('{} {}'.format('1:', sys.argv[res-1]))
else:
    print('{} arguments'.format(res-1))
