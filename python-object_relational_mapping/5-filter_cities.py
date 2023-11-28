#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        """ SELECT cities.name
            FROM cities
            JOIN states
            ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id ASC""", (argv[4],))

    query_rows = cur.fetchall()
    for row in query_rows:
        for name in row:
            print(name, end="" if row ==
                  query_rows[-1] and name == row[-1] else ", ")
    print()

    cur.close()
    db.close()
