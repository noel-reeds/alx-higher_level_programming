#!/usr/bin/python3
import sys
args = len(sys.argv)
res = 0
if args == 1:
    print(res)
else:
    m = 1
    while m < args:
        if args > 1:
            res += int(sys.argv[m])
            m = m + 1
    print(res)


if __name__ == "__main__":
    import sys
