#!/usr/bin/python3
for n in range(0, 9):  # iterate over the first digit.
    for m in range(1, 10):  # iterate over the second digit.
        print("{}".format(n), end="")  # print the first digit.
        print("{}".format(m), end="")  # print the second digit.
        if n == 8 and m == 9:
            continue
        print("{}".format(", "), end="")
