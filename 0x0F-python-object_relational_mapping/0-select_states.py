#!/usr/bin/python3
"""This script gets all states"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """This script would get all states from the database
    listed on the command line 
    including passwords and username
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, username=argv[1], password=argv[2],
        databse=argv[3])
    
    """adding cursor and rules"""
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    db_fetch = db_cursor.fetchall()
    
    """Iterating though db_fetch"""
    for all_rows in db_fetch:
        print(all_rows)
        
    db_cursor.close()
    db.close()