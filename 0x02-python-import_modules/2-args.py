#!/usr/bin/python3
import sys
res = len(sys.argv)
if res == 1:
    print('{} arguments.'.format(res-1))
elif res == 2:
    print('{} argument:'.format(res-1))
else:
    print('{} arguments:'.format(res-1))
m = 1
while m < res:
    if res == 2:
        print('{}: {}'.format(res-1, sys.argv[1]))
    else:
        pass
    m = m + 1
