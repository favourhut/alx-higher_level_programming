#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (argv[4],))
    
    states_row = cur.fetchall()
    for rows in states_row:
        print(rows)

    cur.close()
    conn.close()

