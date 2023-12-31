#!/usr/bin/python3
import sys
res = len(sys.argv)
if res == 1:
    print('{} arguments.'.format(res-1))
elif res == 2:
    print('{} argument:'.format(res-1))
    print('{}: {}'.format(res-1, sys.argv[res-1]))
else:
    print('{} arguments:'.format(res-1))
m = 1
while m < res:
    if res > 2:
        print("{}: {}".format(m, sys.argv[m]))
    m = m + 1

if __name__ == "__main__":
    import sys
