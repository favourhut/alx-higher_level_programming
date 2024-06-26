#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
a script that lists all states
from the database
'''
if __name__ == "__main__":
<<<<<<< HEAD
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()
=======
    """This script would get all states from the database
    listed on the command line 
    including passwords and username
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, username=argv[1], password=argv[2],
        databse=argv[3])
    
    """adding cursor and rules"""
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states")
    db_fetch = db_cursor.fetchall()
    
    """Iterating though db_fetch"""
    for all_rows in db_fetch:
        print(all_rows)
>>>>>>> e3b0f37ea30a05293af008496e17ce0649c65dee