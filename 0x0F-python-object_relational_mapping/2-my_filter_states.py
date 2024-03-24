#!/usr/bin/python3
"""displays all values in the states table """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %search%")
    states = cur.fetchall()
    for state in states:
        print(state)
