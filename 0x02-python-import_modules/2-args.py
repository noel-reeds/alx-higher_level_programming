#!/usr/bin/python3
import sys
res = len(sys.argv)
if res == 1:
    print('{} arguments.'.format(res-1))
elif res == 2:
    print('{} argument:'.format(res-1))
else:
    print('{} arguments:'.format(res-1))
