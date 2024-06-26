#!/usr/bin/python3
"""takes in an argument and displays all values in 
the states table of hbtn_0e_0_usa 
where name matches the argument"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """takes in an argument and displays
    all values in the states table of
    hbtn_0e_0_usa where name matches
    the argument.
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, username=argv[1],
        password=argv[2], database=argv[3])
    
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states WHERE states LIKE '{}'"
                   "ORDER BY states.id ASC".format(argv[4]))
    
    all = db_cursor.fetchall()
    for i in all:
        print(i)
    db_cursor.close()
    db.close()