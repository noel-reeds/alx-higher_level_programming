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
    state = argv[4]
    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        "LEFT JOIN states "
        "ON cities.state_id=states.id "
        "WHERE states.name = %s", (state,)
    )
    cities = cur.fetchall()
    city_list = ""
    for city in cities:
        city_list += city[0] + ", "
    print(city_list[:-2])
