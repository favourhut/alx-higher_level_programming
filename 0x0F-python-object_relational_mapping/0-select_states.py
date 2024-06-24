#!/usr/bin/python3
"""This script would list all 
states from the database named"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """This script takes 3 arguments: 
    mysql username, mysql password and database name.
    """
    data_base = MySQLdb.connect(
        host="localhost", port="3306", username=argv[1], password=argv[2], 
        database=argv[3])
    
    dbase_cursor = data_base.cursor()
    dbase_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    fetch_rows = dbase_cursor.fetchall()
    
    for all_rows in fetch_rows:
        print(all_rows)
        
    """Closing all objects"""    
    dbase_cursor.close()
    data_base.close()