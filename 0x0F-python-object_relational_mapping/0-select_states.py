#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    
    """
    This script list all states from the database
    hbtn_0e_0_usa
    """
    db = MySQLdb.connect(
            host="localhost", username=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3], port="3306")
    
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states")
    
    all_rows = db_cursor.fetchall()
    
    for states_row in all_rows:
        print(states_row)