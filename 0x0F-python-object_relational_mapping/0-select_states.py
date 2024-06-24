#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", username=sys.argv[1], 
                        password=sys.argv[2], database=sys.argv[3], 
                        port="3306")

listAll = db.cusor()
listAll.execute("SELECT * FROM states")
rows = listAll.fetchall()
for row in rows:
    print(row)

listAll.close()    
db.close()