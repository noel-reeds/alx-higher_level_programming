#!/usr/bin/python3
"""displays all values in the states table """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    cur = db.cursor()
    name = argv[4]
    cur.execute("SELECT * FROM states WHERE BINARY name=%s", (name,))
    states = cur.fetchall()
    for state in states:
        print(state)
