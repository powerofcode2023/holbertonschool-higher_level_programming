#!/usr/bin/python3
"""Script to get all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    # Recover argument from user
    user = sys.argv[1]
    pswd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pswd,
        db=db_name
    )

    # Create cursor
    cursor = db.cursor()

    # Executing MySQL Queries in Python
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Display
    all_states = cursor.fetchall()
    for row in all_states:
        print(row)
