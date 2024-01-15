#!/usr/bin/python3

"""
Script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database, search_name = sys.argv[1:]

    with MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306) as con:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s",
                           (search_name,))
            results = cursor.fetchall()
            for result in results:
                print(result)
