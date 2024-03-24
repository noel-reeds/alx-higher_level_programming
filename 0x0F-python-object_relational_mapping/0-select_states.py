#!/usr/bin/python3
import MySQLdb
import sys
# creates a connection
db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
# creates a cursor object
cur = db.cursor
# uses cursor object to execute sql queries
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
states = cur.fetchall()
for state in states:
    print(state)

if __name__ == "__main__":
    import MySQLdb
