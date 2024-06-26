#!/usr/bin/python3
"""takes in an argument and displays all values in 
the states table of hbtn_0e_0_usa 
where name matches the argument"""

import MySQLdb as db
from sys import argv


if __name__ == "__main__":
    """takes in an argument and displays
    all values in the states table of
    hbtn_0e_0_usa where name matches
    the argument.
    """
    database = db.connect(
        host="localhost", port=3306, username=argv[1],
        password=argv[2], dbase=argv[3])
    
    database_cursor = database.cursor()
    database_cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}'"
                            " ORDER BY id ASC".format(argv[4]))
    var_name = database_cursor.fecthall()
    for i in var_name:
        print(i)
        
    database_cursor.close()
    database.close()