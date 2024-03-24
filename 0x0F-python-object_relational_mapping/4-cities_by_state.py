#!/usr/bin/python3
"""Lists all cities in the database"""
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
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)
