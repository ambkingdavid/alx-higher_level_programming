#!/usr/bin/python3
"""script that displays all cities in hbtn_0e_0_usa
    Usage: ./0-select_states.py <mysql username>\
            <mysql password> <database name>\
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            INNER JOIN states\
            ON cities.state_id = states.id\
            ORDER BY id ASC"
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
