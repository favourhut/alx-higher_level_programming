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
        host="localhost", port=3306, user=argv[1],
        passwd=argv[2], db=argv[3])
    
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                      .format(argv[4]))
    
    all_states = db_cursor.fetchall()
    for states in all_states:
        print(states)
    db_cursor.close()
    db.close()