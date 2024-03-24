#!/usr/bin/python3
"""displays all values in the states table """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE '{}'".format(argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
