# Write a script that lists all states from the database hbtn_0e_0_usa:

#     Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
#     You must use the module MySQLdb (import MySQLdb)
#     Your script should connect to a MySQL server running on localhost at port 3306
#     Results must be sorted in ascending order by states.id
#     Results must be displayed as they are in the example below
#     Your code should not be executed when imported

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
    dbase_cursor.execute("SELECT * FROM states")
    
    fetch_rows = dbase_cursor.fetchall()
    
    for all_rows in fetch_rows:
        print(all_rows)
        
    dbase_cursor.close()
    data_base.close()